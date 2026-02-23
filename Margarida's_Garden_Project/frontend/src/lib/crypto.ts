/**
 * Zero Knowledge - criptografia client-side com Web Crypto API.
 * PBKDF2-SHA256 para derivar KEK, AES-256-GCM para credenciais.
 */

const PBKDF2_ITERATIONS = 100_000
const SALT_LENGTH = 32
const IV_LENGTH = 12
const TAG_LENGTH = 128

/** Converte ArrayBuffer para base64 */
function toBase64(buffer: ArrayBuffer): string {
  const bytes = new Uint8Array(buffer)
  let binary = ''
  for (let i = 0; i < bytes.length; i++) {
    binary += String.fromCharCode(bytes[i])
  }
  return btoa(binary)
}

/** Converte base64 para Uint8Array */
function fromBase64(str: string): Uint8Array {
  const binary = atob(str)
  const bytes = new Uint8Array(binary.length)
  for (let i = 0; i < binary.length; i++) {
    bytes[i] = binary.charCodeAt(i)
  }
  return bytes
}

/** Deriva chave AES-256 a partir da senha mestra e salt (base64) */
export async function deriveKey(masterPassword: string, saltBase64: string): Promise<CryptoKey> {
  const salt = fromBase64(saltBase64)
  const enc = new TextEncoder()
  const keyMaterial = await crypto.subtle.importKey(
    'raw',
    enc.encode(masterPassword),
    'PBKDF2',
    false,
    ['deriveBits', 'deriveKey']
  )
  return crypto.subtle.deriveKey(
    {
      name: 'PBKDF2',
      salt,
      iterations: PBKDF2_ITERATIONS,
      hash: 'SHA-256',
    },
    keyMaterial,
    { name: 'AES-GCM', length: 256 },
    false,
    ['encrypt', 'decrypt']
  )
}

/** Criptografa texto com AES-256-GCM */
export async function encrypt(plaintext: string, key: CryptoKey): Promise<string> {
  const iv = crypto.getRandomValues(new Uint8Array(IV_LENGTH))
  const enc = new TextEncoder()
  const ciphertext = await crypto.subtle.encrypt(
    {
      name: 'AES-GCM',
      iv,
      tagLength: TAG_LENGTH,
    },
    key,
    enc.encode(plaintext)
  )
  const combined = new Uint8Array(iv.length + ciphertext.byteLength)
  combined.set(iv)
  combined.set(new Uint8Array(ciphertext), iv.length)
  return toBase64(combined.buffer)
}

/** Descriptografa blob base64 (iv + ciphertext) */
export async function decrypt(encryptedBase64: string, key: CryptoKey): Promise<string> {
  const combined = fromBase64(encryptedBase64)
  const iv = combined.slice(0, IV_LENGTH)
  const ciphertext = combined.slice(IV_LENGTH)
  const decrypted = await crypto.subtle.decrypt(
    {
      name: 'AES-GCM',
      iv,
      tagLength: TAG_LENGTH,
    },
    key,
    ciphertext
  )
  return new TextDecoder().decode(decrypted)
}

import { Link } from 'react-router-dom'

export function Landing() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center relative p-8">
      <h1 className="text-2xl md:text-3xl text-text-dark text-center z-10 mb-8 font-normal tracking-wide">
        Olá <span className="font-semibold text-[#6B9B6B]">Margarida</span>, seja bem-vinda ao seu jardim de senhas!
      </h1>
      <Link
        to="/login"
        className="inline-block px-6 py-3 bg-grass-green text-white rounded-full font-medium mt-4 hover:bg-grass-dark transition-all"
      >
        Entrar no jardim
      </Link>
    </div>
  )
}

import "./globals.css"
import { Inter } from "next/font/google"
import Header from "@/components/Header"
import Sidebar from "@/components/Sidebar"
import type React from "react" // Added import for React

const inter = Inter({ subsets: ["latin"] })

export const metadata = {
  title: "Language Learning Portal",
  description: "A portal for language learning and vocabulary management",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div className="flex h-screen">
          <Sidebar />
          <div className="flex-1 flex flex-col overflow-hidden">
            <Header />
            <main className="flex-1 overflow-x-hidden overflow-y-auto bg-gray-100">{children}</main>
          </div>
        </div>
      </body>
    </html>
  )
}


"use client"

import { useState, useEffect } from "react"
import Link from "next/link"
import { Home, Book, Layers, Activity, Clock, User, Sun, Moon } from "lucide-react"
import { Button } from "@/components/ui/button"
import { useTheme } from "next-themes"

const navItems = [
  { name: "Dashboard", href: "/", icon: Home },
  { name: "Study", href: "/study", icon: Activity },
  { name: "Words", href: "/words", icon: Book },
  { name: "Groups", href: "/groups", icon: Layers },
  { name: "Sessions", href: "/sessions", icon: Clock },
]

export default function Sidebar() {
  const [mounted, setMounted] = useState(false)
  const { theme, setTheme } = useTheme()

  useEffect(() => {
    setMounted(true)
  }, [])

  if (!mounted) {
    return null // Avoid hydration mismatch
  }

  return (
    <div className="bg-[#0A0B0F] text-white w-64 space-y-6 py-7 px-2 absolute inset-y-0 left-0 transform -translate-x-full md:relative md:translate-x-0 transition duration-200 ease-in-out flex flex-col h-full border-r border-gray-800/30">
      <div className="px-4 mb-8">
        <div className="flex justify-between items-center mb-4">
          <h1 className="text-2xl font-bold bg-gradient-to-r from-white to-gray-300 bg-clip-text text-transparent">
            MojiSpace
          </h1>
          <Button
            variant="ghost"
            size="icon"
            className="text-gray-500 hover:text-gray-300 hover:bg-white/5"
            onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
          >
            {theme === 'dark' ? (
              <Sun className="h-5 w-5" />
            ) : (
              <Moon className="h-5 w-5" />
            )}
          </Button>
        </div>
        <p className="text-sm text-gray-500">Japanese Language Learning</p>
      </div>
      
      <nav className="flex-1 px-2">
        {navItems.map((item) => (
          <Link
            key={item.name}
            href={item.href}
            className="flex items-center py-2.5 px-4 rounded-lg transition duration-200 text-gray-400 hover:text-gray-200 hover:bg-white/5 group"
          >
            <item.icon className="h-5 w-5 mr-2 group-hover:text-primary" />
            {item.name}
          </Link>
        ))}
      </nav>

      <div className="px-4 py-4 border-t border-gray-800/30">
        <Button 
          variant="ghost" 
          className="w-full justify-start text-gray-400 hover:text-gray-200 hover:bg-white/5 group"
        >
          <User className="h-5 w-5 mr-2 group-hover:text-primary" />
          Account
        </Button>
      </div>
    </div>
  )
}


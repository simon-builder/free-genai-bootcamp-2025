import Link from "next/link"
import { Home, Book, Layers, Activity, Clock } from "lucide-react"

const navItems = [
  { name: "Dashboard", href: "/", icon: Home },
  { name: "Words", href: "/words", icon: Book },
  { name: "Groups", href: "/groups", icon: Layers },
  { name: "Study", href: "/study", icon: Activity },
  { name: "Sessions", href: "/sessions", icon: Clock },
]

export default function Sidebar() {
  return (
    <div className="bg-gray-800 text-white w-64 space-y-6 py-7 px-2 absolute inset-y-0 left-0 transform -translate-x-full md:relative md:translate-x-0 transition duration-200 ease-in-out">
      <nav>
        {navItems.map((item) => (
          <Link
            key={item.name}
            href={item.href}
            className="block py-2.5 px-4 rounded transition duration-200 hover:bg-gray-700 hover:text-white"
          >
            <item.icon className="inline-block mr-2 h-5 w-5" />
            {item.name}
          </Link>
        ))}
      </nav>
    </div>
  )
}


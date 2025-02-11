import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Clock, Sparkles, BookOpen, BrainCircuit, Pencil } from "lucide-react"

export default function StudyPage() {
  return (
    <div className="p-6">
      <div className="mb-8">
        <div className="flex items-center gap-2 mb-2">
          <Sparkles className="h-6 w-6 text-amber-500 dark:text-amber-400" />
          <span className="text-amber-600 dark:text-amber-400 text-sm font-medium">Study Center</span>
        </div>
        <h1 className="text-4xl font-bold text-gray-900 dark:text-gray-100 mb-2">Study Activities</h1>
        <p className="text-gray-600 dark:text-gray-400">Choose how you want to practice today</p>
        <div className="h-1 w-20 bg-gradient-to-r from-amber-500 to-orange-500 mt-4 rounded-full"></div>

        <div className="mt-8 bg-gradient-to-r from-amber-100/80 to-orange-100/80 dark:from-amber-900/20 dark:to-orange-900/20 border border-amber-200/50 dark:border-amber-700/50 rounded-xl p-4 backdrop-blur-sm flex items-center gap-3">
          <Clock className="h-6 w-6 text-amber-600 dark:text-amber-400" />
          <p className="text-amber-800 dark:text-amber-200">
            Coming Soon! We're working hard to bring you these interactive study features.
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <Card className="hover:shadow-xl transition-all duration-300 border-amber-100/50 dark:border-gray-700 bg-white/80 dark:bg-gray-800 backdrop-blur-sm relative overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-amber-50 to-orange-50 opacity-50 dark:hidden"></div>
          <CardHeader className="flex flex-row items-center space-x-4 pb-2 relative">
            <div className="p-3 bg-gradient-to-br from-amber-100 to-orange-100 dark:bg-gray-700 rounded-xl">
              <BookOpen className="h-7 w-7 text-amber-700" />
            </div>
            <CardTitle className="text-xl text-gray-900 dark:text-gray-100">Flashcards</CardTitle>
          </CardHeader>
          <CardContent className="relative">
            <p className="text-gray-600 dark:text-gray-300 mb-6">Master vocabulary with interactive flashcards. Perfect for quick review sessions.</p>
            <Button 
              disabled 
              className="w-full bg-gradient-to-r from-amber-500 to-orange-500 text-white hover:from-amber-600 hover:to-orange-600 dark:from-amber-600 dark:to-orange-600 dark:hover:from-amber-700 dark:hover:to-orange-700"
            >
              Coming Soon
            </Button>
          </CardContent>
        </Card>

        <Card className="hover:shadow-xl transition-all duration-300 border-amber-100/50 dark:border-gray-700 bg-white/80 dark:bg-gray-800 backdrop-blur-sm relative overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-amber-50 to-orange-50 opacity-50 dark:hidden"></div>
          <CardHeader className="flex flex-row items-center space-x-4 pb-2 relative">
            <div className="p-3 bg-gradient-to-br from-amber-100 to-orange-100 dark:bg-gray-700 rounded-xl">
              <BrainCircuit className="h-7 w-7 text-amber-700" />
            </div>
            <CardTitle className="text-xl text-gray-900 dark:text-gray-100">Multiple Choice</CardTitle>
          </CardHeader>
          <CardContent className="relative">
            <p className="text-gray-600 dark:text-gray-300 mb-6">Test your knowledge with carefully crafted multiple choice questions.</p>
            <Button 
              disabled 
              className="w-full bg-gradient-to-r from-amber-500 to-orange-500 text-white hover:from-amber-600 hover:to-orange-600 dark:from-amber-600 dark:to-orange-600 dark:hover:from-amber-700 dark:hover:to-orange-700"
            >
              Coming Soon
            </Button>
          </CardContent>
        </Card>

        <Card className="hover:shadow-xl transition-all duration-300 border-amber-100/50 dark:border-gray-700 bg-white/80 dark:bg-gray-800 backdrop-blur-sm relative overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-amber-50 to-orange-50 opacity-50 dark:hidden"></div>
          <CardHeader className="flex flex-row items-center space-x-4 pb-2 relative">
            <div className="p-3 bg-gradient-to-br from-amber-100 to-orange-100 dark:bg-gray-700 rounded-xl">
              <Pencil className="h-7 w-7 text-amber-700" />
            </div>
            <CardTitle className="text-xl text-gray-900 dark:text-gray-100">Writing Practice</CardTitle>
          </CardHeader>
          <CardContent className="relative">
            <p className="text-gray-600 dark:text-gray-300 mb-6">Improve your writing skills with guided practice exercises.</p>
            <Button 
              disabled 
              className="w-full bg-gradient-to-r from-amber-500 to-orange-500 text-white hover:from-amber-600 hover:to-orange-600 dark:from-amber-600 dark:to-orange-600 dark:hover:from-amber-700 dark:hover:to-orange-700"
            >
              Coming Soon
            </Button>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}


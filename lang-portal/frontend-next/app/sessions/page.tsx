import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Sparkles, Clock, Calendar, Timer, Brain, ArrowRight } from "lucide-react"

export default function SessionsPage() {
  return (
    <div className="p-6">
      <div className="mb-8">
        <div className="flex items-center gap-2 mb-2">
          <Sparkles className="h-6 w-6 text-amber-500 dark:text-amber-400" />
          <span className="text-amber-600 dark:text-amber-400 text-sm font-medium">Study History</span>
        </div>
        <h1 className="text-4xl font-bold text-gray-900 dark:text-gray-100 mb-2">Learning Sessions</h1>
        <p className="text-gray-600 dark:text-gray-400">Track your study progress and achievements</p>
        <div className="h-1 w-20 bg-gradient-to-r from-amber-500 to-orange-500 mt-4 rounded-full"></div>
      </div>

      <div className="mt-8 bg-gradient-to-r from-amber-100/80 to-orange-100/80 dark:from-amber-900/20 dark:to-orange-900/20 border border-amber-200/50 dark:border-amber-700/50 rounded-xl p-4 backdrop-blur-sm flex items-center gap-3 mb-8">
        <Clock className="h-6 w-6 text-amber-600 dark:text-amber-400" />
        <p className="text-amber-800 dark:text-amber-200">
          Coming Soon! We're working on bringing you detailed study tracking and analytics.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <Card className="hover:shadow-xl transition-all duration-300 border-amber-100/50 dark:border-gray-700 bg-white/80 dark:bg-gray-800 backdrop-blur-sm relative overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-amber-50 to-orange-50 opacity-50 dark:hidden"></div>
          <CardHeader className="flex flex-row items-center space-x-4 pb-2 relative">
            <div className="p-3 bg-gradient-to-br from-amber-100 to-orange-100 dark:bg-gray-700 rounded-xl">
              <Calendar className="h-7 w-7 text-amber-700" />
            </div>
            <CardTitle className="text-xl text-gray-900 dark:text-gray-100">Recent Activity</CardTitle>
          </CardHeader>
          <CardContent className="relative">
            <p className="text-3xl font-bold text-amber-700 dark:text-amber-400">Coming Soon</p>
            <p className="text-gray-600 dark:text-gray-300 mt-2">View your recent study sessions</p>
          </CardContent>
        </Card>

        <Card className="hover:shadow-xl transition-all duration-300 border-amber-100/50 dark:border-gray-700 bg-white/80 dark:bg-gray-800 backdrop-blur-sm relative overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-amber-50 to-orange-50 opacity-50 dark:hidden"></div>
          <CardHeader className="flex flex-row items-center space-x-4 pb-2 relative">
            <div className="p-3 bg-gradient-to-br from-amber-100 to-orange-100 dark:bg-gray-700 rounded-xl">
              <Timer className="h-7 w-7 text-amber-700" />
            </div>
            <CardTitle className="text-xl text-gray-900 dark:text-gray-100">Study Time</CardTitle>
          </CardHeader>
          <CardContent className="relative">
            <p className="text-3xl font-bold text-amber-700 dark:text-amber-400">Coming Soon</p>
            <p className="text-gray-600 dark:text-gray-300 mt-2">Track your study duration</p>
          </CardContent>
        </Card>

        <Card className="hover:shadow-xl transition-all duration-300 border-amber-100/50 dark:border-gray-700 bg-white/80 dark:bg-gray-800 backdrop-blur-sm relative overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-amber-50 to-orange-50 opacity-50 dark:hidden"></div>
          <CardHeader className="flex flex-row items-center space-x-4 pb-2 relative">
            <div className="p-3 bg-gradient-to-br from-amber-100 to-orange-100 dark:bg-gray-700 rounded-xl">
              <Brain className="h-7 w-7 text-amber-700" />
            </div>
            <CardTitle className="text-xl text-gray-900 dark:text-gray-100">Performance</CardTitle>
          </CardHeader>
          <CardContent className="relative">
            <p className="text-3xl font-bold text-amber-700 dark:text-amber-400">Coming Soon</p>
            <p className="text-gray-600 dark:text-gray-300 mt-2">View your learning progress</p>
          </CardContent>
        </Card>
      </div>

      <div className="mt-8">
        <Card className="hover:shadow-xl transition-all duration-300 border-amber-100/50 dark:border-gray-700 bg-white/80 dark:bg-gray-800 backdrop-blur-sm relative overflow-hidden">
          <div className="absolute inset-0 bg-gradient-to-br from-amber-50 to-orange-50 opacity-50 dark:hidden"></div>
          <CardHeader className="relative">
            <CardTitle className="text-xl text-gray-900 dark:text-gray-100">Recent Sessions</CardTitle>
            <p className="text-gray-600 dark:text-gray-400 mt-1">Your study history will appear here</p>
          </CardHeader>
          <CardContent className="relative">
            <div className="text-center py-12">
              <Clock className="h-12 w-12 text-amber-500 dark:text-amber-400 mx-auto mb-4" />
              <p className="text-lg font-medium text-gray-900 dark:text-gray-100 mb-2">No Sessions Yet</p>
              <p className="text-gray-600 dark:text-gray-400 mb-6">Start studying to track your progress</p>
              <Button 
                disabled
                className="bg-gradient-to-r from-amber-500 to-orange-500 text-white hover:from-amber-600 hover:to-orange-600 dark:from-amber-600 dark:to-orange-600 dark:hover:from-amber-700 dark:hover:to-orange-700"
              >
                Start New Session
                <ArrowRight className="h-4 w-4 ml-2" />
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}


import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

export default function StudyPage() {
  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">Study Activities</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Flashcards</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="mb-4">Practice with flashcards</p>
            <Button>Start</Button>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Multiple Choice</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="mb-4">Test your knowledge with multiple choice questions</p>
            <Button>Start</Button>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Writing Practice</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="mb-4">Practice writing words and phrases</p>
            <Button>Start</Button>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}


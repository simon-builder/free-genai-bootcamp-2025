import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"

export default function Dashboard() {
  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Total Words</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-4xl font-bold">500</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Groups</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-4xl font-bold">10</p>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <CardTitle>Study Sessions</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-4xl font-bold">25</p>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}


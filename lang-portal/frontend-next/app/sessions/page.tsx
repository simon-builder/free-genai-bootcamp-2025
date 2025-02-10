import { Button } from "@/components/ui/button"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"

export default function SessionsPage() {
  return (
    <div className="p-6">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Study Sessions</h1>
        <Button>Start New Session</Button>
      </div>
      <Table>
        <TableHeader>
          <TableRow>
            <TableHead>Date</TableHead>
            <TableHead>Duration</TableHead>
            <TableHead>Words Reviewed</TableHead>
            <TableHead>Correct</TableHead>
            <TableHead>Incorrect</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          <TableRow>
            <TableCell>2023-05-15</TableCell>
            <TableCell>30 minutes</TableCell>
            <TableCell>50</TableCell>
            <TableCell>40</TableCell>
            <TableCell>10</TableCell>
          </TableRow>
          {/* Add more rows as needed */}
        </TableBody>
      </Table>
    </div>
  )
}


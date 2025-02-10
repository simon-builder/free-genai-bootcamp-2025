'use client'

export default function ErrorDisplay({ error }: { error: Error }) {
  console.error('Client-side error:', error)
  return (
    <div className="p-4 bg-red-50 text-red-700 rounded">
      Error: {error.message}
    </div>
  )
} 
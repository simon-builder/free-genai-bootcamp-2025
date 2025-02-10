"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from "@/components/ui/dialog"
import { createWord } from "@/lib/api"

export default function AddWordForm() {
  const [isOpen, setIsOpen] = useState(false)
  const [wordData, setWordData] = useState({ kanji: "", romaji: "", english: "" })
  const router = useRouter()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    await createWord(wordData)
    setIsOpen(false)
    setWordData({ kanji: "", romaji: "", english: "" })
    router.refresh()
  }

  return (
    <Dialog open={isOpen} onOpenChange={setIsOpen}>
      <DialogTrigger asChild>
        <Button>Add New Word</Button>
      </DialogTrigger>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Add New Word</DialogTitle>
        </DialogHeader>
        <form onSubmit={handleSubmit} className="space-y-4">
          <Input
            placeholder="Kanji"
            value={wordData.kanji}
            onChange={(e) => setWordData({ ...wordData, kanji: e.target.value })}
          />
          <Input
            placeholder="Romaji"
            value={wordData.romaji}
            onChange={(e) => setWordData({ ...wordData, romaji: e.target.value })}
          />
          <Input
            placeholder="English"
            value={wordData.english}
            onChange={(e) => setWordData({ ...wordData, english: e.target.value })}
          />
          <div className="flex justify-end space-x-2">
            <Button type="button" variant="outline" onClick={() => setIsOpen(false)}>
              Cancel
            </Button>
            <Button type="submit">Save</Button>
          </div>
        </form>
      </DialogContent>
    </Dialog>
  )
}
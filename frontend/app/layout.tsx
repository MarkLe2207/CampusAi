import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'CampusAI',
  description: 'Intelligent campus assistant platform',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}

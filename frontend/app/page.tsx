export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 bg-gradient-to-b from-white to-gray-100">
      <div className="text-center">
        <h1 className="text-4xl font-bold text-gray-900 mb-4">
          Welcome to CampusAI
        </h1>
        <p className="text-xl text-gray-600 mb-8">
          Intelligent campus assistant platform
        </p>
        <div className="inline-block bg-white rounded-lg shadow-lg p-6">
          <p className="text-gray-700">
            Frontend is ready. Backend will be available soon.
          </p>
        </div>
      </div>
    </main>
  )
}

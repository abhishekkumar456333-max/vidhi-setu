import React from 'react';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null, errorInfo: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error("Uncaught error:", error, errorInfo);
    this.setState({ error, errorInfo });
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="p-8 max-w-2xl mx-auto mt-12 bg-red-50 border border-red-200 rounded-xl">
          <h2 className="text-xl font-bold text-red-800 mb-4">Something went wrong.</h2>
          <details open className="whitespace-pre-wrap text-sm text-red-700 font-mono bg-white p-4 rounded border border-red-300 mb-4">
            <summary className="cursor-pointer font-bold mb-2">Error Details</summary>
            {this.state.error && this.state.error.toString()}
            <br /><br />
            {this.state.errorInfo && this.state.errorInfo.componentStack}
          </details>
          <button 
            onClick={() => window.location.reload()}
            className="mt-6 px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700"
          >
            Reload Page
          </button>
        </div>
      );
    }

    return this.props.children; 
  }
}

export default ErrorBoundary;

import React from 'react';
import { FadeIn, SlideUp } from '../ui/motion';
import { ChevronLeft, Scale, ShieldCheck, Users, Zap, BarChart3 } from 'lucide-react';

const AboutPage = ({ onBack, hasAnalysis, onDashboard }) => {
  return (
    <div className="min-h-screen bg-zinc-50 font-sans text-zinc-900">
      <nav className="max-w-7xl mx-auto px-6 py-10 flex justify-between items-center bg-white border-b-2 border-zinc-100 sticky top-0 z-50 h-40">
        <div className="flex items-center gap-5 cursor-pointer" onClick={onBack}>
          <div className="w-24 h-24 rounded-full overflow-hidden border-4 border-zinc-50 shadow-lg bg-white flex items-center justify-center">
            <img src="/favicon.jpeg" alt="Vidhi Setu Logo" className="w-[90%] h-[90%] object-contain" />
          </div>
          <div className="flex flex-col">
            <h1 className="text-3xl font-black tracking-tighter text-zinc-950">Vidhi Setu</h1>
            <span className="text-xs font-bold text-zinc-400 uppercase tracking-widest px-1">Our Story</span>
          </div>
        </div>
        <div className="flex items-center gap-6">
          {hasAnalysis && (
            <button 
              onClick={onDashboard}
              className="flex items-center gap-2 text-sm font-bold text-zinc-900 bg-white border border-zinc-200 px-4 py-2 rounded-full shadow-sm hover:shadow-md transition-all active:scale-95"
            >
              <BarChart3 className="w-4 h-4" /> Go to Dashboard
            </button>
          )}
          <button 
            onClick={onBack}
            className="flex items-center gap-2 text-sm font-medium text-zinc-500 hover:text-zinc-900 transition-colors"
          >
            <ChevronLeft className="w-4 h-4" /> Back to Home
          </button>
        </div>
      </nav>

      <main className="max-w-4xl mx-auto px-6 py-20">
        <SlideUp>
          <h2 className="text-5xl md:text-6xl font-black tracking-tighter mb-8 bg-black text-transparent bg-clip-text">
            Bridging the Gap Between Law and People.
          </h2>
          <p className="text-xl text-zinc-600 leading-relaxed mb-12">
            Vidhi Setu is built by a team of legal tech enthusiasts dedicated to making Indian contract law accessible, transparent, and safe for freelancers and small businesses. We believe that understanding a contract shouldn't require a law degree.
          </p>
        </SlideUp>

        <FadeIn delay={0.2}>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-12 mb-20">
            <div className="space-y-4">
              <div className="w-12 h-12 bg-zinc-900 rounded-xl flex items-center justify-center text-white">
                <ShieldCheck className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold">Privacy First</h3>
              <p className="text-zinc-500">
                Your data stays with you. We process everything in ephemeral memory and never store your contract contents.
              </p>
            </div>
            <div className="space-y-4">
              <div className="w-12 h-12 bg-zinc-100 rounded-xl flex items-center justify-center text-zinc-900">
                <Scale className="w-6 h-6" />
              </div>
              <h3 className="text-xl font-bold">Indian Law Expertise</h3>
              <p className="text-zinc-500">
                Grounded specifically in the Indian Contract Act and relevant statutes for precise local context.
              </p>
            </div>
          </div>
        </FadeIn>

        <SlideUp delay={0.4}>
          <section className="bg-zinc-900 text-white p-12 rounded-3xl shadow-xl overflow-hidden relative">
            <div className="absolute top-0 right-0 w-64 h-64 bg-zinc-800 rounded-full -mr-32 -mt-32 blur-3xl opacity-50" />
            <div className="relative z-10">
              <h3 className="text-2xl font-bold mb-6">Our Mission</h3>
              <p className="text-zinc-400 text-lg leading-relaxed mb-8">
                Our mission is to provide simple, trustworthy insights that empower individuals to sign with confidence, knowing exactly what they're agreeing to. We're democratizing legal intelligence, one clause at a time.
              </p>
              <div className="flex items-center gap-4">
                <div className="flex -space-x-2">
                  <div className="w-10 h-10 rounded-full border-2 border-zinc-900 bg-zinc-700" title="Legal Expert" />
                  <div className="w-10 h-10 rounded-full border-2 border-zinc-900 bg-zinc-600" title="AI Engineer" />
                  <div className="w-10 h-10 rounded-full border-2 border-zinc-900 bg-zinc-500" title="UI Designer" />
                </div>
                <span className="text-sm font-medium text-zinc-400">Founded by legal tech enthusiasts.</span>
              </div>
            </div>
          </section>
        </SlideUp>

        <SlideUp delay={0.6}>
          <div className="mt-20 text-center">
            <h3 className="text-zinc-400 text-sm font-bold tracking-widest uppercase mb-4">The Values</h3>
            <div className="flex flex-wrap justify-center gap-8">
              {['Transparency', 'Security', 'Simplicity', 'Precision'].map((value) => (
                <div key={value} className="flex items-center gap-2">
                  <span className="w-2 h-2 rounded-full bg-zinc-400" />
                  <span className="font-bold text-lg">{value}</span>
                </div>
              ))}
            </div>
          </div>
        </SlideUp>
      </main>

      <footer className="max-w-7xl mx-auto px-6 py-12 border-t border-zinc-100 text-center text-sm text-zinc-400">
        <p>© 2026 Vidhi Setu. Made for the Indian creative community.</p>
      </footer>
    </div>
  );
};

export default AboutPage;

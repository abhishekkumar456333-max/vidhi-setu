import React from 'react';
import { Twitter, Linkedin, Github } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="bg-zinc-950 text-zinc-400 py-16 border-t border-zinc-900">
      <div className="max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-4 gap-12">
        
        {/* Brand */}
        <div className="space-y-4">
           <div className="flex items-center gap-2">
             <div className="w-8 h-8 bg-white rounded-lg flex items-center justify-center text-zinc-950 font-bold text-lg">V</div>
             <span className="text-xl font-bold text-white tracking-tight">Vidhi Setu</span>
           </div>
           <p className="text-sm leading-relaxed">
             Empowering legal professionals with AI-driven insights. 
             Precision, speed, and security for the modern age.
           </p>
           <div className="flex gap-4 pt-2">
             <a href="#" className="hover:text-white transition-colors"><Twitter className="w-5 h-5" /></a>
             <a href="#" className="hover:text-white transition-colors"><Linkedin className="w-5 h-5" /></a>
             <a href="#" className="hover:text-white transition-colors"><Github className="w-5 h-5" /></a>
           </div>
        </div>

        {/* Product */}
        <div>
          <h4 className="text-white font-semibold mb-6">Product</h4>
          <ul className="space-y-3 text-sm">
            <li><a href="#" className="hover:text-white transition-colors">Features</a></li>
            <li><a href="#" className="hover:text-white transition-colors">Pricing</a></li>
            <li><a href="#" className="hover:text-white transition-colors">Enterprise</a></li>
            <li><a href="#" className="hover:text-white transition-colors">Changelog</a></li>
          </ul>
        </div>

        {/* Company */}
        <div>
          <h4 className="text-white font-semibold mb-6">Company</h4>
          <ul className="space-y-3 text-sm">
            <li><a href="#" className="hover:text-white transition-colors">About Us</a></li>
            <li><a href="#" className="hover:text-white transition-colors">Careers</a></li>
            <li><a href="#" className="hover:text-white transition-colors">Blog</a></li>
            <li><a href="#" className="hover:text-white transition-colors">Contact</a></li>
          </ul>
        </div>

        {/* Legal */}
        <div>
          <h4 className="text-white font-semibold mb-6">Legal</h4>
          <ul className="space-y-3 text-sm">
            <li><a href="#" className="hover:text-white transition-colors">Privacy Policy</a></li>
            <li><a href="#" className="hover:text-white transition-colors">Terms of Service</a></li>
            <li><a href="#" className="hover:text-white transition-colors">Cookie Policy</a></li>
            <li><a href="#" className="hover:text-white transition-colors">Security</a></li>
          </ul>
        </div>

      </div>
      <div className="max-w-7xl mx-auto px-6 mt-16 pt-8 border-t border-zinc-900 text-sm text-center md:text-left flex flex-col md:flex-row justify-between items-center">
        <p>© 2026 Vidhi Setu. All rights reserved.</p>
        <p className="mt-2 md:mt-0">Designed with precision.</p>
      </div>
    </footer>
  );
};

export default Footer;

import { useState, useEffect } from 'react';

const JarvisCore = () => {
  const [isActive, setIsActive] = useState(false);
  const [systemStatus, setSystemStatus] = useState('INITIALIZING...');

  useEffect(() => {
    const statusCycle = ['INITIALIZING...', 'ANALYZING...', 'PROCESSING...', 'READY', 'SCANNING...'];
    let statusIndex = 0;

    const statusInterval = setInterval(() => {
      setSystemStatus(statusCycle[statusIndex]);
      statusIndex = (statusIndex + 1) % statusCycle.length;
    }, 2000);

    const pulseInterval = setInterval(() => {
      setIsActive(prev => !prev);
    }, 4000);

    return () => {
      clearInterval(statusInterval);
      clearInterval(pulseInterval);
    };
  }, []);

  return (
    <div className="flex flex-col items-center justify-center h-full relative">
      {/* Background Matrix Effect */}
      <div className="absolute inset-0 overflow-hidden opacity-10">
        {[...Array(6)].map((_, i) => (
          <div 
            key={i}
            className="absolute w-px h-full bg-gradient-to-b from-transparent via-robot-cyan to-transparent matrix-rain"
            style={{ 
              left: `${15 + i * 15}%`,
              animationDelay: `${i * 1.3}s`
            }}
          />
        ))}
      </div>

      <div className="relative z-10">
        {/* Outer electromagnetic field */}
        <div className="absolute -inset-16 core-ring rounded-full rotating-circle opacity-30"></div>
        
        {/* Main rotating rings */}
        <div className="absolute inset-0 w-96 h-96 core-ring rounded-full rotating-circle"></div>
        <div className="absolute inset-6 core-ring rounded-full rotating-reverse opacity-70"></div>
        <div className="absolute inset-12 core-ring rounded-full rotating-fast opacity-50"></div>
        
        {/* Inner core housing */}
        <div className={`w-96 h-96 rounded-full flex items-center justify-center transition-all duration-1000 relative ${
          isActive ? 'pulse-glow' : ''
        }`}>
          {/* Core chamber */}
          <div className="w-48 h-48 rounded-full hologram-effect flex flex-col items-center justify-center relative overflow-hidden">
            {/* JARVIS text with hologram effect */}
            <div className="text-center z-20">
              <h1 className="text-2xl font-orbitron font-bold hologram-text tracking-wider">
                J.A.R.V.I.S
              </h1>
              <div className="text-xs font-rajdhani text-robot-cyan mt-2 opacity-80 font-medium tracking-widest">
                {systemStatus}
              </div>
            </div>
            
            {/* Central pulse core */}
            <div className={`w-6 h-6 rounded-full mt-4 transition-all duration-500 ${
              isActive ? 'bg-robot-cyan shadow-lg shadow-robot-cyan/50 animate-pulse' : 'bg-robot-blue/60'
            }`}></div>
            
            {/* Scanning lines */}
            <div className="absolute inset-0 scan-line opacity-30">
              <div className="w-full h-px bg-robot-cyan absolute top-1/4"></div>
              <div className="w-full h-px bg-robot-cyan absolute top-2/4"></div>
              <div className="w-full h-px bg-robot-cyan absolute top-3/4"></div>
            </div>
          </div>
        </div>
        
        {/* Floating data particles */}
        <div className="absolute top-8 left-12 w-3 h-3 bg-robot-cyan rounded-full float-particle opacity-80"></div>
        <div className="absolute top-16 right-8 w-2 h-2 bg-robot-electric rounded-full float-particle opacity-60" style={{ animationDelay: '1s' }}></div>
        <div className="absolute bottom-12 left-8 w-2.5 h-2.5 bg-robot-cyan rounded-full float-particle opacity-70" style={{ animationDelay: '2s' }}></div>
        <div className="absolute bottom-8 right-16 w-2 h-2 bg-robot-blue rounded-full float-particle opacity-80" style={{ animationDelay: '3s' }}></div>
        <div className="absolute top-1/2 left-4 w-1.5 h-1.5 bg-robot-electric rounded-full float-particle opacity-60" style={{ animationDelay: '1.5s' }}></div>
        <div className="absolute top-1/2 right-4 w-2.5 h-2.5 bg-robot-cyan rounded-full float-particle opacity-70" style={{ animationDelay: '0.5s' }}></div>
        
        {/* Data streams */}
        <div className="absolute top-24 left-20 w-16 h-px bg-gradient-to-r from-transparent via-robot-cyan to-transparent opacity-60"></div>
        <div className="absolute bottom-32 right-24 w-20 h-px bg-gradient-to-l from-transparent via-robot-electric to-transparent opacity-50"></div>
      </div>
      
      {/* Status indicator */}
      <div className="mt-12 text-center z-10">
        <p className="text-muted-foreground font-rajdhani text-sm tracking-wide">
          Just A Rather Very Intelligent System
        </p>
        <div className="flex items-center justify-center mt-6 gap-3">
          <div className="w-2 h-2 bg-robot-cyan rounded-full animate-pulse"></div>
          <div className="w-2 h-2 bg-robot-electric rounded-full animate-pulse" style={{ animationDelay: '0.5s' }}></div>
          <div className="w-2 h-2 bg-robot-blue rounded-full animate-pulse" style={{ animationDelay: '1s' }}></div>
        </div>
        <div className="mt-4 font-orbitron text-xs text-robot-cyan tracking-widest opacity-70">
          [ SYSTEM OPERATIONAL ]
        </div>
      </div>
    </div>
  );
};

export default JarvisCore;
import SystemMetrics from '@/components/SystemMetrics';
import JarvisCore from '@/components/JarvisCore';
import NetworkInfo from '@/components/NetworkInfo';

const Index = () => {
  return (
    <div className="min-h-screen bg-background p-4 relative overflow-hidden">
      {/* Background Tech Grid */}
      <div className="fixed inset-0 opacity-5" style={{
        backgroundImage: `
          linear-gradient(hsl(var(--robot-cyan)) 1px, transparent 1px),
          linear-gradient(90deg, hsl(var(--robot-cyan)) 1px, transparent 1px)
        `,
        backgroundSize: '50px 50px'
      }}></div>
      
      {/* Main Dashboard Grid */}
      <div className="grid grid-cols-12 gap-6 h-screen relative z-10">
        {/* Left Panel - System Diagnostics */}
        <div className="col-span-3 space-y-4 overflow-y-auto scrollbar-thin scrollbar-track-transparent scrollbar-thumb-robot-cyan/30">
          <SystemMetrics />
        </div>
        
        {/* Center Panel - Jarvis Core */}
        <div className="col-span-6 flex items-center justify-center">
          <JarvisCore />
        </div>
        
        {/* Right Panel - Network & Visual Feed */}
        <div className="col-span-3 space-y-4 overflow-y-auto scrollbar-thin scrollbar-track-transparent scrollbar-thumb-robot-cyan/30">
          <NetworkInfo />
        </div>
      </div>
      
      {/* Corner Status Indicators */}
      <div className="fixed top-4 left-4 z-20">
        <div className="flex items-center gap-2 px-3 py-1 bg-card/80 rounded border border-robot-cyan/30 backdrop-blur-sm">
          <div className="w-2 h-2 bg-robot-cyan rounded-full animate-pulse"></div>
          <span className="text-xs font-orbitron text-robot-cyan tracking-wider">SYSTEM ONLINE</span>
        </div>
      </div>
      
      <div className="fixed top-4 right-4 z-20">
        <div className="flex items-center gap-2 px-3 py-1 bg-card/80 rounded border border-robot-cyan/30 backdrop-blur-sm">
          <span className="text-xs font-orbitron text-robot-cyan tracking-wider">v2.1.47</span>
        </div>
      </div>
    </div>
  );
};

export default Index;

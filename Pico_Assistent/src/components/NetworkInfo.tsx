import { Wifi, Globe, Signal, Video, Radio, Monitor } from 'lucide-react';
import { useEffect, useState } from 'react';

interface NetworkData {
  ipAddress: string;
  wifiName: string;
  wifiSpeed: number;
  signalStrength: number;
  isConnected: boolean;
  bandwidth: number;
  latency: number;
}

const NetworkInfo = () => {
  const [networkData, setNetworkData] = useState<NetworkData>({
    ipAddress: '192.168.1.154',
    wifiName: 'STARK_INDUSTRIES',
    wifiSpeed: 856,
    signalStrength: 87,
    isConnected: true,
    bandwidth: 1.2,
    latency: 12
  });

  const [streamStatus, setStreamStatus] = useState('CONNECTING...');

  useEffect(() => {
    const interval = setInterval(() => {
      setNetworkData(prev => ({
        ...prev,
        wifiSpeed: Math.max(400, Math.min(1000, prev.wifiSpeed + (Math.random() - 0.5) * 40)),
        signalStrength: Math.max(70, Math.min(100, prev.signalStrength + (Math.random() - 0.5) * 8)),
        bandwidth: Math.max(0.5, Math.min(2.5, prev.bandwidth + (Math.random() - 0.5) * 0.2)),
        latency: Math.max(5, Math.min(25, prev.latency + (Math.random() - 0.5) * 3))
      }));
    }, 3000);

    const statusCycle = ['CONNECTING...', 'BUFFERING...', 'LIVE FEED', 'RECORDING', 'ANALYZING'];
    let statusIndex = 0;
    const statusInterval = setInterval(() => {
      setStreamStatus(statusCycle[statusIndex]);
      statusIndex = (statusIndex + 1) % statusCycle.length;
    }, 4000);

    return () => {
      clearInterval(interval);
      clearInterval(statusInterval);
    };
  }, []);

  const InfoCard = ({ 
    title, 
    value, 
    icon: Icon, 
    color,
    subtitle 
  }: { 
    title: string; 
    value: string | number; 
    icon: any; 
    color: string;
    subtitle?: string;
  }) => (
    <div className="metric-card data-stream group p-3">
      <div className="flex items-center gap-2 mb-2">
        <div className="p-1.5 rounded bg-secondary/50">
          <Icon className={`h-4 w-4 ${color}`} />
        </div>
        <div className="flex-1">
          <p className="text-xs font-rajdhani font-medium text-foreground tracking-wide">{title}</p>
          {subtitle && (
            <p className="text-xs font-orbitron text-robot-cyan tracking-wider opacity-70">{subtitle}</p>
          )}
        </div>
      </div>
      <p className="text-sm font-orbitron font-bold text-foreground pl-7">{value}</p>
    </div>
  );

  return (
    <div className="h-screen flex flex-col overflow-hidden">
      <style >{`
        .metric-card {
          background: rgba(17, 24, 39, 0.8);
          border: 1px solid rgba(34, 211, 238, 0.3);
          border-radius: 8px;
          backdrop-filter: blur(8px);
          position: relative;
        }
        .data-stream::before {
          content: '';
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          height: 1px;
          background: linear-gradient(90deg, transparent, rgba(34, 211, 238, 0.5), transparent);
          animation: scan 2s linear infinite;
        }
        @keyframes scan {
          0% { transform: translateX(-100%); opacity: 0; }
          50% { opacity: 1; }
          100% { transform: translateX(100%); opacity: 0; }
        }
        .scan-line {
          animation: scan 3s linear infinite;
        }
        .text-robot-cyan { color: hsl(var(--robot-cyan, 187 85% 53%)); }
        .text-robot-blue { color: hsl(var(--robot-blue, 217 91% 60%)); }
        .text-robot-electric { color: hsl(var(--robot-electric, 142 76% 36%)); }
        .text-foreground { color: hsl(var(--foreground, 0 0% 98%)); }
        .bg-secondary { background: hsl(var(--secondary, 240 4% 16%)); }
        .text-muted-foreground { color: hsl(var(--muted-foreground, 240 5% 65%)); }
      `}</style>

      {/* Header */}
      <div className="flex items-center gap-3 p-4 border-b border-robot-cyan/30">
        <Radio className="h-5 w-5 text-robot-cyan" />
        <h2 className="text-lg font-orbitron font-bold text-foreground tracking-wider">NETWORK STATUS</h2>
        <span className="ml-auto text-sm font-orbitron text-robot-cyan">V2.14.1</span>
      </div>
      
      {/* Content - Flexible with proper spacing */}
      <div className="flex-1 p-3 space-y-3 overflow-auto">
        {/* Network Cards - 2x2 Grid */}
        <div className="grid grid-cols-2 gap-3">
          <InfoCard
            title="IP ADDRESS"
            value={networkData.ipAddress}
            icon={Globe}
            color="text-robot-blue"
            subtitle="IPV4"
          />
          
          <InfoCard
            title="NETWORK ID"
            value={networkData.wifiName}
            icon={Wifi}
            color="text-robot-cyan"
            subtitle="5GHz BAND"
          />
          
          <InfoCard
            title="THROUGHPUT"
            value={`${Math.round(networkData.wifiSpeed)} Mbps`}
            icon={Signal}
            color="text-robot-electric"
            subtitle="DOWNLOAD"
          />
          
          <InfoCard
            title="BANDWIDTH"
            value={`${networkData.bandwidth.toFixed(1)} GB/s`}
            icon={Signal}
            color="text-robot-cyan"
            subtitle="REAL-TIME"
          />
        </div>

        {/* Signal Quality */}
        <div className="metric-card data-stream group p-4">
          <div className="flex items-center justify-between mb-3">
            <div className="flex items-center gap-3">
              <div className="p-1.5 rounded bg-secondary/50">
                <Signal className="h-4 w-4 text-robot-cyan" />
              </div>
              <div>
                <span className="text-sm font-rajdhani font-medium text-foreground tracking-wide">SIGNAL</span>
                <div className="text-xs font-orbitron text-robot-cyan tracking-wider opacity-70">
                  WIRELESS
                </div>
              </div>
            </div>
            <div className="text-right">
              <span className="text-lg font-orbitron font-bold text-foreground">{Math.round(networkData.signalStrength)}%</span>
              <div className="text-xs font-orbitron text-robot-cyan tracking-wider">
                {Math.round(networkData.latency)}ms
              </div>
            </div>
          </div>
          
          <div className="relative">
            <div className="w-full bg-secondary/50 rounded-full h-2 overflow-hidden">
              <div 
                className={`h-2 rounded-full transition-all duration-1000 relative ${
                  networkData.signalStrength > 80 ? 'bg-gradient-to-r from-robot-cyan to-robot-electric' : 
                  networkData.signalStrength > 60 ? 'bg-gradient-to-r from-robot-blue to-robot-cyan' : 
                  'bg-gradient-to-r from-robot-warn to-robot-danger'
                }`}
                style={{ width: `${networkData.signalStrength}%` }}
              >
                <div className="absolute inset-0 bg-white/20 animate-pulse"></div>
              </div>
            </div>
          </div>
        </div>

        {/* Camera Feed - Simplified */}
        <div className="metric-card data-stream flex-1 p-4 min-h-0">
          <div className="flex items-center justify-between mb-3">
            <div className="flex items-center gap-3">
              <div className="p-1.5 rounded bg-secondary/50">
                <Monitor className="h-4 w-4 text-robot-cyan" />
              </div>
              <div>
                <span className="text-sm font-rajdhani font-medium text-foreground tracking-wide">VISUAL FEED</span>
                <div className="text-xs font-orbitron text-robot-cyan tracking-wider opacity-70">
                  {streamStatus}
                </div>
              </div>
            </div>
            <div className="flex items-center gap-2">
              <div className="w-2 h-2 bg-robot-cyan rounded-full animate-pulse"></div>
              <span className="text-xs font-orbitron text-robot-cyan tracking-wider">ACTIVE</span>
            </div>
          </div>
          
          <div className="aspect-video bg-secondary/30 rounded-lg flex items-center justify-center relative overflow-hidden border border-robot-cyan/30">
            {/* Background Grid Effect */}
            <div className="absolute inset-0 opacity-20" style={{
              backgroundImage: `
                linear-gradient(hsl(var(--robot-cyan) / 0.1) 1px, transparent 1px),
                linear-gradient(90deg, hsl(var(--robot-cyan) / 0.1) 1px, transparent 1px)
              `,
              backgroundSize: '20px 20px'
            }}></div>
            
            <div className="absolute inset-0 bg-gradient-to-br from-robot-blue/10 to-robot-cyan/10"></div>
            
            <div className="text-center z-20 relative">
              <Video className="h-12 w-12 text-robot-cyan mx-auto mb-2" />
              <p className="text-sm font-orbitron text-foreground font-medium tracking-wider">CAMERA FEED</p>
              <p className="text-xs font-rajdhani text-muted-foreground mt-1">1920×1080 • 60fps • H.264</p>
              <div className="mt-2 flex items-center justify-center gap-2">
                <div className="w-1 h-1 bg-robot-cyan rounded-full animate-pulse"></div>
                <span className="text-xs font-orbitron text-robot-cyan tracking-widest">REC</span>
              </div>
            </div>
            
            {/* Scanning Effects */}
            <div className="absolute top-0 left-0 w-full h-px bg-robot-cyan/60 animate-pulse"></div>
            <div className="absolute bottom-0 left-0 w-full h-px bg-robot-cyan/60 animate-pulse" style={{ animationDelay: '1s' }}></div>
            <div className="absolute top-0 left-0 w-px h-full bg-robot-cyan/60 animate-pulse" style={{ animationDelay: '0.5s' }}></div>
            <div className="absolute top-0 right-0 w-px h-full bg-robot-cyan/60 animate-pulse" style={{ animationDelay: '1.5s' }}></div>
            
            {/* Moving scan line */}
            <div className="absolute inset-0 flex items-center">
              <div className="w-full h-px bg-gradient-to-r from-transparent via-robot-cyan/60 to-transparent scan-line"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default NetworkInfo;
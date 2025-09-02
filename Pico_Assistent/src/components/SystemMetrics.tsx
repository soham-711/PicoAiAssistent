import {
  Activity,
  Thermometer,
  Cloud,
  Droplets,
  Wind,
  Eye,
} from "lucide-react";
import { useEffect, useState } from "react";

interface MetricData {
  cpu: number;
  ram: number;
  temperature: number;
}

interface WeatherData {
  temperature: number;
  humidity: number;
  windSpeed: number;
  condition: string;
}

const SystemMetrics = () => {
  const [metrics, setMetrics] = useState<MetricData>({
    cpu: 78,
    ram: 79,
    temperature: 58,
  });

  const [weather, setWeather] = useState<WeatherData>({
    temperature: 24,
    humidity: 65,
    windSpeed: 12,
    condition: "CLEAR",
  });

  useEffect(() => {
    const interval = setInterval(() => {
      setMetrics((prev) => ({
        cpu: Math.max(15, Math.min(90, prev.cpu + (Math.random() - 0.5) * 8)),
        ram: Math.max(25, Math.min(95, prev.ram + (Math.random() - 0.5) * 6)),
        temperature: Math.max(
          35,
          Math.min(75, prev.temperature + (Math.random() - 0.5) * 4)
        ),
      }));

      setWeather((prev) => ({
        temperature: Math.max(
          15,
          Math.min(35, prev.temperature + (Math.random() - 0.5) * 2)
        ),
        humidity: Math.max(
          30,
          Math.min(90, prev.humidity + (Math.random() - 0.5) * 4)
        ),
        windSpeed: Math.max(
          5,
          Math.min(25, prev.windSpeed + (Math.random() - 0.5) * 3)
        ),
        condition: ["CLEAR", "CLOUDY", "WINDY", "HUMID"][
          Math.floor(Math.random() * 4)
        ],
      }));
    }, 2500);

    return () => clearInterval(interval);
  }, []);

  const MetricCard = ({
    title,
    value,
    unit,
    icon: Icon,
    color,
    status,
  }: {
    title: string;
    value: number;
    unit: string;
    icon: any;
    color: string;
    status?: string;
  }) => (
    <div className="metric-card data-stream group p-4 hover:border-cyan-400/50 transition-all duration-300 relative ">
      {/* Scan line effect */}
      <div className="absolute top-0 left-0 w-full h-0.5 bg-gradient-to-r from-transparent via-cyan-400/60 to-transparent animate-pulse"></div>

      <div className="flex items-start justify-between mb-3">
        <div className="flex items-center gap-3">
          <div className="p-2 rounded bg-secondary/50">
            <Icon className={`h-4 w-4 ${color}`} />
          </div>
          <div>
            <h3 className="text-xs font-rajdhani font-medium text-foreground tracking-wider">
              {title}
            </h3>
            {status && (
              <div className="text-xs text-robot-cyan font-orbitron tracking-wider opacity-70 mt-0.5">
                {status}
              </div>
            )}
          </div>
        </div>
        <div
          className={`text-xs font-orbitron tracking-wider px-2 py-1 rounded ${
            value > 80
              ? "text-robot-warn bg-robot-warn/10"
              : value > 60
              ? "text-robot-cyan bg-robot-cyan/10"
              : "text-robot-blue bg-robot-blue/10"
          }`}
        >
          {value > 80 ? "HIGH" : value > 60 ? "NORM" : "LOW"}
        </div>
      </div>

      <div className="space-y-3">
        <div className="flex items-baseline gap-2">
          <span className="text-2xl font-orbitron font-bold text-foreground">
            {Math.round(value)}
          </span>
          <span className="text-sm font-rajdhani text-muted-foreground">
            {unit}
          </span>
        </div>

        <div className="relative">
          <div className="w-full bg-secondary/50 rounded-full h-2 overflow-hidden">
            <div
              className={`h-2 rounded-full transition-all duration-1000 relative ${
                value > 80
                  ? "bg-gradient-to-r from-robot-warn to-robot-danger"
                  : value > 60
                  ? "bg-gradient-to-r from-robot-cyan to-robot-electric"
                  : "bg-gradient-to-r from-robot-blue to-robot-cyan"
              }`}
              style={{ width: `${value}%` }}
            >
              <div className="absolute inset-0 bg-white/20 animate-pulse"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen flex flex-col p-4">
      <style>{`
  @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;500;600;700&display=swap');
  .font-orbitron { font-family: 'Orbitron', monospace; }
  .font-rajdhani { font-family: 'Rajdhani', sans-serif; }
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
  .text-robot-cyan { color: hsl(var(--robot-cyan, 187 85% 53%)); }
  .text-robot-blue { color: hsl(var(--robot-blue, 217 91% 60%)); }
  .text-robot-electric { color: hsl(var(--robot-electric, 142 76% 36%)); }
  .text-robot-warn { color: hsl(var(--robot-warn, 45 93% 58%)); }
  .text-robot-danger { color: hsl(var(--robot-danger, 0 84% 60%)); }
  .text-foreground { color: hsl(var(--foreground, 0 0% 98%)); }
  .bg-secondary { background: hsl(var(--secondary, 240 4% 16%)); }
  .text-muted-foreground { color: hsl(var(--muted-foreground, 240 5% 65%)); }
  .bg-robot-cyan\/10 { background: hsla(187, 85%, 53%, 0.1); }
  .bg-robot-warn\/10 { background: hsla(45, 93%, 58%, 0.1); }
  .bg-robot-blue\/10 { background: hsla(217, 91%, 60%, 0.1); }

  /* 🚀 Hide scrollbar globally */
  ::-webkit-scrollbar { display: none; }
  * { -ms-overflow-style: none; scrollbar-width: none; }
`}</style>

      {/* Header */}
      <div className="flex items-center gap-3 mb-6 pb-4 border-b border-robot-cyan/20">
        <div className="p-2 rounded bg-secondary/50">
          <Eye className="h-5 w-5 text-robot-cyan" />
        </div>
        <div>
          <h1 className="text-lg font-orbitron font-bold text-foreground tracking-wider">
            SYSTEM DIAGNOSTICS
          </h1>
          <p className="text-xs text-robot-cyan font-rajdhani tracking-wider">
            REAL-TIME MONITORING
          </p>
        </div>
      </div>

      {/* Metrics */}
      <div className="flex-1 space-y-4">
        <MetricCard
          title="CPU UTILIZATION"
          value={metrics.cpu}
          unit="%"
          icon={Activity}
          color="text-robot-cyan"
          status="CORE-8"
        />

        <MetricCard
          title="RAM UTILIZATION"
          value={metrics.ram}
          unit="%"
          icon={Activity}
          color="text-robot-electric"
          status="256GB/512GB"
        />

        <MetricCard
          title="SYSTEM TEMPERATURE"
          value={metrics.temperature}
          unit="°C"
          icon={Thermometer}
          color={
            metrics.temperature > 65 ? "text-robot-warn" : "text-robot-cyan"
          }
          status="COOLING ACTIVE"
        />

        {/* Weather Section */}
        <div className="metric-card data-stream group p-4 hover:border-cyan-400/50 transition-all duration-300 relative overflow-hidden">
          <div className="absolute top-0 left-0 w-full h-0.5 bg-gradient-to-r from-transparent via-cyan-400/60 to-transparent animate-pulse"></div>

          <div className="flex items-center gap-3 mb-4">
            <div className="p-2 rounded bg-secondary/50">
              <Cloud className="h-5 w-5 text-robot-cyan" />
            </div>
            <div>
              <h3 className="text-xs font-rajdhani font-medium text-foreground tracking-wider">
                WEATHER UPDATE
              </h3>
              <div className="text-xs text-robot-electric font-orbitron tracking-wider opacity-70">
                {weather.condition}
              </div>
            </div>
          </div>

          <div className="grid grid-cols-3 gap-3">
            <div className="bg-secondary/30 rounded-lg p-3 text-center hover:bg-robot-cyan/10 transition-colors">
              <div className="text-xs font-orbitron text-robot-cyan tracking-wider mb-1">
                TEMP
              </div>
              <div className="text-lg font-rajdhani font-bold text-foreground">
                {weather.temperature}°C
              </div>
            </div>
            <div className="bg-secondary/30 rounded-lg p-3 text-center hover:bg-robot-cyan/10 transition-colors">
              <div className="text-xs font-orbitron text-robot-cyan tracking-wider mb-1">
                HUMID
              </div>
              <div className="text-lg font-rajdhani font-bold text-foreground">
                {weather.humidity}%
              </div>
            </div>
            <div className="bg-secondary/30 rounded-lg p-3 text-center hover:bg-robot-cyan/10 transition-colors">
              <div className="text-xs font-orbitron text-robot-cyan tracking-wider mb-1">
                WIND
              </div>
              <div className="text-lg font-rajdhani font-bold text-foreground">
                {Math.round(weather.windSpeed)}
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Footer Status */}
      <div className="mt-4 pt-4 border-t border-robot-cyan/20">
        <div className="flex justify-between items-center bg-secondary/40 rounded p-3">
          <div className="flex items-center gap-3">
            <div className="w-2 h-2 bg-robot-cyan rounded-full animate-pulse"></div>
            <span className="text-xs font-orbitron text-foreground tracking-wider">
              SYSTEM STATUS
            </span>
          </div>
          <span className="text-xs font-orbitron text-robot-cyan tracking-wider">
            OPERATIONAL
          </span>
        </div>

        <div className="mt-3 text-center">
          <div className="flex justify-center items-center gap-2">
            <Cloud className="h-4 w-4 text-robot-cyan" />
            <span className="text-xs font-rajdhani text-robot-cyan tracking-wider">
              {new Date().toLocaleString("en-IN", {
                weekday: "short",
                day: "2-digit",
                month: "short",
                year: "numeric",
                hour: "2-digit",
                minute: "2-digit",
                hour12: true,
              })}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SystemMetrics;

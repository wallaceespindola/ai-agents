---
name: frontend-performance
description: Optimize frontend applications for bundle size, rendering performance, and user experience
---

# Frontend Performance Skill

## When to Use This Skill

- Analyzing and reducing bundle size
- Optimizing React component rendering
- Implementing code splitting and lazy loading
- Improving Core Web Vitals scores
- Reducing memory usage and leaks
- Image optimization and lazy loading
- CSS and JavaScript minification
- Performance monitoring and metrics

## Quick Start

```
/frontend-performance <application_or_component_area>
```

**Example**:
```
/frontend-performance Next.js dashboard with heavy data tables and charts
```

## How It Works

The skill provides comprehensive frontend performance optimization:

### 1. Bundle Size Optimization
- **Code Splitting**: Route-based and component-based splitting
- **Tree Shaking**: Remove unused code
- **Minification**: Compress JavaScript and CSS
- **Lazy Loading**: Load code when needed
- **Dynamic Imports**: On-demand module loading

### 2. React Performance
- **Memoization**: React.memo, useMemo, useCallback
- **Virtual Lists**: Virtualization for large lists
- **Suspense**: Boundary-based code splitting
- **Profiling**: React DevTools profiler
- **Render Optimization**: Prevent unnecessary renders

### 3. Core Web Vitals
- **LCP (Largest Contentful Paint)**: Loading performance
- **FID (First Input Delay)**: Responsiveness
- **CLS (Cumulative Layout Shift)**: Visual stability
- **INP (Interaction to Next Paint)**: Overall responsiveness

### 4. Image Optimization
- **Format Selection**: WebP, AVIF, JPEG, PNG
- **Responsive Images**: srcset and sizes
- **Lazy Loading**: IntersectionObserver
- **Compression**: Reduce file size
- **CDN Delivery**: Geographically optimized serving

### 5. Caching Strategies
- **Browser Cache**: Cache-Control headers
- **Service Workers**: Offline support
- **HTTP Caching**: ETag and Last-Modified
- **API Caching**: Request deduplication
- **Storage**: localStorage, IndexedDB

### 6. JavaScript Optimization
- **Parsing**: Defer non-critical scripts
- **Execution**: Web Workers for heavy computation
- **Event Delegation**: Reduce event listeners
- **Debouncing**: Throttle expensive operations
- **Memory Management**: Garbage collection

### 7. Monitoring & Metrics
- **Web Vitals**: Real User Monitoring (RUM)
- **Performance API**: Browser timing data
- **Lighthouse**: Automated auditing
- **Network Waterfall**: Request analysis
- **Error Tracking**: Performance degradation

## Configuration

**Next.js (next.config.js)**:
```javascript
module.exports = {
  reactStrictMode: true,
  compress: true,
  swcMinify: true,
  images: {
    formats: ['image/avif', 'image/webp'],
  },
  experimental: {
    optimizePackageImports: [],
  },
};
```

**Webpack (webpack.config.js)**:
```javascript
module.exports = {
  mode: 'production',
  optimization: {
    splitChunks: {
      chunks: 'all',
    },
    minimize: true,
  },
};
```

**Vite (vite.config.ts)**:
```typescript
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
        },
      },
    },
  },
});
```

## Examples

### Example 1: Code Splitting and Lazy Loading

```typescript
// ❌ NO CODE SPLITTING
import { Dashboard } from './Dashboard';
import { Analytics } from './Analytics';
import { Settings } from './Settings';
import { Reports } from './Reports';

export const App = () => {
  const [page, setPage] = React.useState<'dashboard' | 'analytics' | 'settings' | 'reports'>('dashboard');

  let content;
  switch (page) {
    case 'dashboard':
      content = <Dashboard />;
      break;
    case 'analytics':
      content = <Analytics />;
      break;
    case 'settings':
      content = <Settings />;
      break;
    case 'reports':
      content = <Reports />;
      break;
  }

  return (
    <div>
      <nav>
        <button onClick={() => setPage('dashboard')}>Dashboard</button>
        <button onClick={() => setPage('analytics')}>Analytics</button>
        <button onClick={() => setPage('settings')}>Settings</button>
        <button onClick={() => setPage('reports')}>Reports</button>
      </nav>
      {content}
    </div>
  );
};


// ✅ WITH CODE SPLITTING
const Dashboard = React.lazy(() => import('./Dashboard'));
const Analytics = React.lazy(() => import('./Analytics'));
const Settings = React.lazy(() => import('./Settings'));
const Reports = React.lazy(() => import('./Reports'));

const Loading = () => <div>Loading...</div>;

export const App = () => {
  const [page, setPage] = React.useState<'dashboard' | 'analytics' | 'settings' | 'reports'>('dashboard');

  let content;
  switch (page) {
    case 'dashboard':
      content = <Dashboard />;
      break;
    case 'analytics':
      content = <Analytics />;
      break;
    case 'settings':
      content = <Settings />;
      break;
    case 'reports':
      content = <Reports />;
      break;
  }

  return (
    <div>
      <nav>
        <button onClick={() => setPage('dashboard')}>Dashboard</button>
        <button onClick={() => setPage('analytics')}>Analytics</button>
        <button onClick={() => setPage('settings')}>Settings</button>
        <button onClick={() => setPage('reports')}>Reports</button>
      </nav>
      <React.Suspense fallback={<Loading />}>
        {content}
      </React.Suspense>
    </div>
  );
};


// ✅ NEXT.JS DYNAMIC IMPORTS
import dynamic from 'next/dynamic';

const Dashboard = dynamic(() => import('./Dashboard'));
const Analytics = dynamic(() => import('./Analytics'));

export const App = () => {
  // Same usage as above
};
```

### Example 2: React.memo and useMemo

```typescript
// ❌ UNNECESSARY RE-RENDERS
interface ListItemProps {
  item: Item;
  onDelete: (id: number) => void;
}

const ListItem = ({ item, onDelete }: ListItemProps) => {
  console.log('ListItem render:', item.id);
  return (
    <li>
      {item.name}
      <button onClick={() => onDelete(item.id)}>Delete</button>
    </li>
  );
};

export const List = ({ items, onDelete }: { items: Item[]; onDelete: (id: number) => void }) => {
  // onDelete created new each render - causes ListItem re-renders
  return (
    <ul>
      {items.map(item => (
        <ListItem key={item.id} item={item} onDelete={onDelete} />
      ))}
    </ul>
  );
};


// ✅ OPTIMIZED
const ListItem = React.memo<ListItemProps>(({ item, onDelete }) => {
  return (
    <li>
      {item.name}
      <button onClick={() => onDelete(item.id)}>Delete</button>
    </li>
  );
});

export const List = ({ items, onDelete }: { items: Item[]; onDelete: (id: number) => void }) => {
  const memoizedOnDelete = React.useCallback(onDelete, [onDelete]);

  const memoizedItems = React.useMemo(() => items, [items]);

  return (
    <ul>
      {memoizedItems.map(item => (
        <ListItem key={item.id} item={item} onDelete={memoizedOnDelete} />
      ))}
    </ul>
  );
};
```

### Example 3: Image Optimization

```typescript
// ❌ UNOPTIMIZED IMAGES
export const ImageGallery = () => {
  return (
    <div>
      <img src="/images/large-image.png" alt="Gallery" />
      <img src="/images/background.jpg" alt="Background" />
    </div>
  );
};


// ✅ OPTIMIZED WITH NEXT.JS IMAGE
import Image from 'next/image';

export const ImageGallery = () => {
  return (
    <div>
      <Image
        src="/images/gallery.webp"
        alt="Gallery"
        width={800}
        height={600}
        sizes="(max-width: 768px) 100vw, 800px"
        priority
        quality={80}
      />
      <Image
        src="/images/background.webp"
        alt="Background"
        width={1920}
        height={1080}
        sizes="(max-width: 768px) 100vw, 1920px"
        loading="lazy"
        quality={75}
      />
    </div>
  );
};


// ✅ RESPONSIVE IMAGES WITH SRCSET
export const ResponsiveImage = () => {
  return (
    <picture>
      <source
        media="(max-width: 640px)"
        srcSet="/images/small.webp 640w, /images/small@2x.webp 1280w"
        type="image/webp"
      />
      <source
        media="(max-width: 1024px)"
        srcSet="/images/medium.webp 1024w, /images/medium@2x.webp 2048w"
        type="image/webp"
      />
      <source
        srcSet="/images/large.webp 1920w, /images/large@2x.webp 3840w"
        type="image/webp"
      />
      <img
        src="/images/fallback.jpg"
        alt="Responsive"
        loading="lazy"
      />
    </picture>
  );
};
```

### Example 4: Virtual List for Large Datasets

```typescript
// ❌ RENDERING ALL ITEMS
export const UserList = ({ users }: { users: User[] }) => {
  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
};
// Problem: Rendering 10,000 items creates 10,000 DOM nodes


// ✅ VIRTUALIZED LIST
import { FixedSizeList } from 'react-window';

export const VirtualUserList = ({ users }: { users: User[] }) => {
  const Row = ({ index, style }: { index: number; style: React.CSSProperties }) => (
    <div style={style}>
      {users[index].name}
    </div>
  );

  return (
    <FixedSizeList
      height={600}
      itemCount={users.length}
      itemSize={35}
      width="100%"
    >
      {Row}
    </FixedSizeList>
  );
};
// Only renders visible items (e.g., 20 items)
```

### Example 5: Performance Monitoring

```typescript
// ✅ WEB VITALS MONITORING
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

export const initPerformanceMonitoring = () => {
  getCLS(metric => console.log('CLS:', metric.value));
  getFID(metric => console.log('FID:', metric.value));
  getFCP(metric => console.log('FCP:', metric.value));
  getLCP(metric => console.log('LCP:', metric.value));
  getTTFB(metric => console.log('TTFB:', metric.value));
};


// ✅ CUSTOM PERFORMANCE TRACKING
export const usePerformanceTrack = (componentName: string) => {
  React.useEffect(() => {
    const startTime = performance.now();

    return () => {
      const endTime = performance.now();
      console.log(`${componentName} rendered in ${endTime - startTime}ms`);

      // Send to analytics
      fetch('/api/metrics', {
        method: 'POST',
        body: JSON.stringify({
          component: componentName,
          duration: endTime - startTime,
          timestamp: new Date()
        })
      });
    };
  }, [componentName]);
};

// Usage in component
export const MyComponent = () => {
  usePerformanceTrack('MyComponent');
  return <div>Component content</div>;
};


// ✅ PERFORMANCE.NOW() MEASUREMENTS
export const measureBlockingCode = async () => {
  performance.mark('start-processing');

  // Expensive operation
  await processLargeDataset();

  performance.mark('end-processing');
  performance.measure('data-processing', 'start-processing', 'end-processing');

  const measure = performance.getEntriesByName('data-processing')[0];
  console.log(`Processing took ${measure.duration}ms`);
};
```

### Example 6: Bundle Analysis

```javascript
// webpack.config.js with bundle analyzer
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
  plugins: [
    new BundleAnalyzerPlugin({
      analyzerMode: 'static',
      openAnalyzer: false,
      reportFilename: 'bundle-report.html'
    })
  ]
};

// Analyze bundle: webpack-bundle-analyzer dist/main.js
```

## Best Practices

### 1. Performance Budget
```javascript
// Define acceptable sizes for bundles
const performanceBudget = {
  'js': 150 * 1024,      // 150KB
  'css': 50 * 1024,      // 50KB
  'images': 100 * 1024   // 100KB
};
```

### 2. Audit Regularly
- Run Lighthouse monthly
- Monitor Core Web Vitals
- Track bundle size changes
- Profile in production-like environments

### 3. Prioritization
- Fix LCP first (biggest user impact)
- Then FID/INP (responsiveness)
- Then CLS (stability)

### 4. Testing Performance
```typescript
describe('Performance', () => {
  test('component renders within 100ms', () => {
    const start = performance.now();
    render(<Component />);
    const duration = performance.now() - start;
    expect(duration).toBeLessThan(100);
  });
});
```

## Integration with Other Skills

- **`javascript-code-review`**: Performance review in code reviews
- **`nextjs-setup`**: Next.js optimization features
- **`cicd-pipeline-setup`**: Performance regression testing
- **`frontend-monitoring`**: Real user monitoring


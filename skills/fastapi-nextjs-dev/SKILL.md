---
name: fastapi-nextjs-dev
description: Development workflow for FastAPI + Next.js projects (hiddenbeer and skipy). Use when building features, fixing bugs, or setting up development environment for these full-stack apps.
user-invocable: true
allowed-tools: Bash(make *), Bash(uv *), Bash(pnpm *), Bash(npm *), Read, Grep, Write, Edit
---

# FastAPI + Next.js Development Workflow

Your FastAPI + Next.js projects (hiddenbeer, skipy) follow this architecture pattern:

## Backend Architecture (FastAPI)

### Tech Stack
- **Framework**: FastAPI (async Python web framework)
- **Database**: MongoDB with Beanie ODM (async via Motor)
- **Auth**: JWT + refresh tokens, OTP-based (no passwords)
- **Background Jobs**: APScheduler
- **External Services**: Brevo (email), Bird (SMS)

### Structure
```
backend/
├── app/
│   ├── models/         # Beanie ODM models (MongoDB documents)
│   ├── routes/         # API endpoints
│   ├── schemas/        # Pydantic request/response models
│   ├── services/       # Business logic
│   └── core/           # Config, security, database
```

### Development Commands
- **hiddenbeer**: `make dev-backend` (port 8004)
- **skipy**: `make dev-api` or `cd apps/skipy-api && uv run uvicorn app.main:app --reload` (port 8100)

### Key Patterns
1. **Database Operations**: Always use `await` with Beanie models (async ODM)
   ```python
   user = await User.find_one(User.email == email)
   await user.save()
   ```

2. **Indexes**: MongoDB uses 2dsphere (geospatial), TTL, and compound indexes
   - Geospatial queries for location-based features
   - TTL indexes for auto-expiring documents (OTP codes, reservations)
   - Compound indexes for fraud prevention

3. **Error Handling**: Use FastAPI HTTPException
   ```python
   from fastapi import HTTPException, status
   raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
   ```

## Frontend Architecture (Next.js)

### Tech Stack
- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript (strict mode)
- **Styling**: TailwindCSS + shadcn/ui components
- **State Management**: TanStack React Query (server state)
- **Maps**: Leaflet (react-leaflet)
- **QR Codes**: qrcode.react, @zxing/browser

### Structure
```
frontend/
├── src/
│   ├── app/            # Next.js 15 App Router pages
│   ├── components/     # React components (shadcn/ui + custom)
│   ├── lib/            # Utilities, API client, hooks
│   └── types/          # TypeScript types
```

### Development Commands
- **hiddenbeer**: `make dev-frontend` (port 3004)
- **skipy**: `make dev-client` (port 8080), `make dev-admin` (port 8070)

### Key Patterns
1. **API Calls**: Use TanStack React Query for server state
   ```typescript
   const { data, isLoading } = useQuery({
     queryKey: ['beers'],
     queryFn: () => fetch('/api/beers').then(r => r.json())
   })
   ```

2. **Data Fetching**: Server Components (RSC) by default, Client Components with 'use client'
   - Server Components: Direct API calls, no loading states needed
   - Client Components: TanStack Query, interactive UI

3. **Styling**: shadcn/ui + Tailwind utility classes
   ```tsx
   <Button variant="outline" size="lg" className="w-full">
     Click Me
   </Button>
   ```

## Common Development Tasks

### Adding a New Feature
1. **Define the API contract**: Update/create Pydantic schemas
2. **Backend**: Create route → service → model operations
3. **Frontend**: Create component → API hook → UI integration
4. **Test**: `make test` (backend pytest), manual testing (frontend)

### Working with MongoDB
- **Geospatial queries**: Use `$near` or `$geoWithin` with 2dsphere indexes
- **Relationships**: Beanie supports links and backrefs
- **Aggregations**: Use Motor's aggregate() for complex queries

### Environment Variables
- Both projects use `.env` files (gitignored)
- Look for `.env.example` or `.env.local.example` for required vars
- hiddenbeer and skipy have BE (Belgium) and BR (Brazil) variants

## Before Committing
```bash
make lint          # Lint both backend and frontend
make format        # Format code (black, prettier)
make test          # Run tests (pytest for backend)
```

## Common Issues

1. **MongoDB connection**: Ensure MongoDB is running (`docker ps` or local instance)
2. **Port conflicts**: Check if ports 8004/8100/3004/8080 are available
3. **Environment vars**: Missing .env file or variables
4. **Dependencies**: Run `make setup` (hiddenbeer) or `pnpm install` (skipy)

## Database Tips

- **hiddenbeer**: Geospatial features (bars near user location)
- **skipy**: Multi-tenant architecture (restaurant isolation)
- Both use fraud prevention: compound indexes prevent duplicate actions
- TTL indexes automatically clean up expired documents (OTPs, reservations)

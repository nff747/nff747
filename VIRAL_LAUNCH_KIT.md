# 🚀 Master Viral Open Source Distribution Playbook // nff747

This document is your tactical execution guide to distribute your 10 deep-tech repositories, hit **#1 on Hacker News**, trend on **GitHub Trending**, and maximize organic traffic and stars while cementing the **"Powered by nff747"** branding.

---

## 📅 The 2-Week Launch Schedule

Never launch all repositories at once. Launch in 4 staged waves to maintain momentum across developer communities:

| Wave | Date / Day | Featured Project | Target Community | Core Metric Goal |
| :--- | :--- | :--- | :--- | :--- |
| **Wave 1** | **Tuesday 8:15 AM EST** | **`auto-rig-web`** | Hacker News, Twitter, r/threejs, r/gamedev | 1,000+ stars, HN Top 5 |
| **Wave 2** | **Thursday 8:30 AM EST** | **`aerocache`** | Hacker News, Twitter, r/java, r/programming | 800+ stars, HN Top 10 |
| **Wave 3** | **Next Tuesday 8:15 AM EST**| **`splat-bvh-core`** | Twitter, r/webgpu, r/graphics, NeRF Discord | 600+ stars, GitHub Trending |
| **Wave 4** | **Next Thursday 8:30 AM EST**| **`helix-lsm` & `swarm-refactor`** | r/rust, r/LocalLLaMA, Twitter tech circles | 500+ stars |

---

## 🎯 Lead Horse #1: `auto-rig-web`
- **Hook**: Zero-click humanoid 3D rigging in a Web Worker (No Blender, No Mixamo, No server).
- **Kit Location**: [`auto-rig-web/LAUNCH.md`](https://github.com/nff747/auto-rig-web/blob/main/LAUNCH.md)
- **Hacker News Title**: `Show HN: Auto-Rig Web – Zero-click 3D humanoid rigging in a Web Worker`
- **Key Visual**: Screen recording dropping `.glb` model into browser viewport with instant bone snap.

---

## 🎯 Lead Horse #2: `aerocache`
- **Hook**: Redis-compatible in-memory cache in Java reaching 13,000,000 ops/sec with 0.10µs P99 latency and 0 GC pauses via `sun.misc.Unsafe`.
- **Kit Location**: [`aerocache/LAUNCH.md`](https://github.com/nff747/aerocache/blob/main/LAUNCH.md)
- **Hacker News Title**: `Show HN: AeroCache – 13M ops/sec Redis-compatible cache in Java (Zero GC pauses)`
- **Key Visual**: ASCII / SVG chart showing latency comparison vs standard Redis and Java HashMap under GC stress.

---

## 🎯 Lead Horse #3: `splat-bvh-core`
- **Hook**: Karras 2012 GPU LBVH tree builder in WebGPU WGSL with Bitonic sorting for 10M 3D Gaussian Splats.
- **Kit Location**: [`splat-bvh-core/LAUNCH.md`](https://github.com/nff747/splat-bvh-core/blob/main/LAUNCH.md)
- **Hacker News Title**: `Show HN: Splat-BVH – Karras 2012 GPU LBVH builder in pure WGSL for 3D Gaussians`

---

## 🎯 Lead Horse #4: `helix-lsm`
- **Hook**: Distributed lock-free LSM-tree database engine in Rust with multi-level streaming compaction and consistent hashing.
- **Kit Location**: [`helix-lsm/LAUNCH.md`](https://github.com/nff747/helix-lsm/blob/main/LAUNCH.md)
- **Hacker News Title**: `Show HN: HelixLSM – Lock-free distributed LSM-tree database engine in Rust`

---

## 🎯 Lead Horse #5: `swarm-refactor`
- **Hook**: Actor-model multi-agent orchestrator for closed-loop code self-healing with AST security gates and POSIX resource limits.
- **Kit Location**: [`swarm-refactor/LAUNCH.md`](https://github.com/nff747/swarm-refactor/blob/main/LAUNCH.md)
- **Hacker News Title**: `Show HN: SwarmRefactor – Actor Model multi-agent framework for iterative code self-healing`

---

## 📢 The Viral Amplification Protocol

1. **Submit to Curated Developer Newsletters**:
   - [JavaScript Weekly](https://javascriptweekly.com/submit) (for `auto-rig-web`, `spatial-glass-ui`)
   - [Rust Weekly](https://this-week-in-rust.org/) (for `helix-lsm`, `nova-wasm`)
   - [Console.dev](https://console.dev/) (features open-source dev tools)
   - [TLDR Tech](https://tldr.tech/) (newsletter with 1.2M+ developers)
2. **Product Hunt**:
   - Create a Product Hunt upcoming page or launch `auto-rig-web` on a Wednesday at 12:01 AM PST.
3. **LinkedIn Engineering Write-up**:
   - Publish high-resolution system design diagrams explaining the zero-allocation off-heap memory model of `aerocache` or the Karras BVH sorting passes in `splat-bvh-core`.

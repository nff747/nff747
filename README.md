# nff747

Systems & Graphics Engineer specializing in **WebGPU compute**, **browser-native AI acceleration**, and **lock-free concurrency**. Building high-throughput runtimes, low-level data structures, and real-time physical simulations that push the boundaries of browser and edge runtimes.

---

### ⚡ Selected Open-Source Work

#### 🎮 WebGPU & Compute Shaders
* **[webgpu-vram-pager](https://github.com/nff747/webgpu-vram-pager)** — Virtual memory paging & ring buffer for executing 8B+ LLMs in-browser, bypassing WebGPU `maxStorageBufferBindingSize` limits.
* **[splat-bvh-core](https://github.com/nff747/splat-bvh-core)** — WebGPU-accelerated parallel Radix Sort and Linear BVH (LBVH) generator for 10M+ 3D Gaussian Splats with sub-millisecond raycasting.
* **[ocean-fft-wgsl](https://github.com/nff747/ocean-fft-wgsl)** — Real-time Tessendorf spectral ocean wave simulation and Phillips spectrum IFFT in pure WebGPU compute shaders.
* **[radiance-cascades-wgsl](https://github.com/nff747/radiance-cascades-wgsl)** — Real-time Radiance Cascades global illumination solver in WGSL with directional radiance filtering.
* **[tensor-cloth-wgsl](https://github.com/nff747/tensor-cloth-wgsl)** — Extended Position-Based Dynamics (XPBD) cloth and soft-body simulation engine on WebGPU.
* **[marching-cubes-wgsl](https://github.com/nff747/marching-cubes-wgsl)** — GPU-driven Marching Cubes isosurface extraction and mesh generation in WGSL.

#### ⚙️ Low-Level Concurrency & Systems
* **[turbo-ring-ipc](https://github.com/nff747/turbo-ring-ipc)** — Wait-free SPSC circular ring buffer and Dmitry Vyukov MPMC ticket queue over `SharedArrayBuffer` with cache-line false-sharing isolation (>20M ops/s).
* **[hyper-hnsw-core](https://github.com/nff747/hyper-hnsw-core)** — SIMD-accelerated Hierarchical Navigable Small World (HNSW) vector search index for high-dimensional embeddings.
* **[helix-lsm](https://github.com/nff747/helix-lsm)** — Log-Structured Merge-tree (LSM) storage engine with atomic SSTable compaction, Bloom filters, and zero-allocation point lookups.
* **[synapse-quant](https://github.com/nff747/synapse-quant)** — Hardware-accelerated 1.58-bit ternary matrix-vector GEMM engine in WGSL and WebAssembly.
* **[edge-uuidv7](https://github.com/nff747/edge-uuidv7)** — Zero-allocation, monotonic bitwise UUIDv7 generator for edge runtimes.

---

### 🛠️ Core Technical Stack

* **Languages**: Rust, WGSL, TypeScript, C++, Python
* **Graphics & Compute**: WebGPU, WGSL Compute Shaders, WebGL2, Three.js, SIMD/WASM
* **Concurrency & Systems**: Lock-Free Ring Buffers, Atomics, SharedArrayBuffer, Memory Barriers, Cache-Line Optimization
* **Algorithms**: Linear BVH, Morton Codes, Radix Sort, HNSW Graphs, FFT Spectral Solvers, XPBD

---

<p align="center">
  <img src="https://github-readme-stats-eight-theta.vercel.app/api?username=nff747&show_icons=true&hide_border=true&bg_color=0d1117&title_color=58a6ff&icon_color=58a6ff&text_color=c9d1d9" alt="GitHub Stats" width="48%"/>
  <img src="https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username=nff747&layout=compact&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9" alt="Top Languages" width="48%"/>
</p>

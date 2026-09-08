# Audit: stabilizer-shell decomposition of SCOV4

**Date:** 2026-08-06  
**Object:**
MATH_THEOREM_STABILIZER_SHELL_DECOMPOSITION_OF_SCOV4_20260806.md  
**Verdict:** **PASS AS A DETERMINISTIC REDUCTION WITH RAD4 CLOSED;
ANG4 COEFFICIENT TRANSFER REMAINS OPEN.**

## 1. Shell geometry

At distance \(\ell\) from \(x\), a state is determined by an
\(\ell\)-subset removed from \(x\) and an \(\ell\)-subset inserted from
its complement. The stabilizer-shell graph is therefore the half-half
product of \(J(q,\ell)\) and \(J(k-q,\ell)\). Its gap is exactly (1.5).
For \(\ell=O(d)=o(k)\), the inverse gap is \(O(\ell)=O(d)\).

## 2. Covariance factor

For every accepted edge \(G\),

\[
 \left(\sum_{y\in G}u_y\right)^2
 \le |G\cap T|\sum_{y\in G\cap T}u_y^2.
\]

After summing \(a_G\), this gives (2.5). The one-resource stopped upper
bound is sufficient; no lower bound on the mass of an individual
stratum is used.

## 3. Boundary identity

The transpositions used inside a shell lie in the stabilizer of \(x\).
Hence \(z_{\tau A}(x)=z_A(x)\), and reindexing \(B=\tau A\) gives (3.3)
without an output-transport error. This fails for a general full-Johnson
transposition and is the reason the shell decomposition is necessary.

## 4. Scope

The radial calculation uses the literal FIFO track table, not merely an
average codegree. A simple track pays
\(\sum_\ell N_\ell^{-1}=O(k^{-2})\). A repeated-distance plateau of
multiplicity \(m\) occurs only at distance at least \(m-O(1)\), so
\(m^2/N_\ell=O(k^{-2})\); the finitely many small \(m\) cases are absorbed
in the constant. Weighted Cauchy then gives
\(\operatorname {Rad}_x\le Ck^{-2}g_x^2\), and the exact identity
\(\sum g_x^2/c_x=\sum g_x+\Psi_i\) verifies (4.11).
The \(d^{-2}\) prefactor means that even the deterministic
\(O(\log d)\) occupation envelope under PCAP is harmless; no unproved
unweighted pair-potential occupation estimate is required for RAD4.

The theorem does not assert:

* that every composite blocker incidence lies at distance \(O(d)\);
* that rigid or cross-half shells are negligible dynamically;
* that complete-row polarization by itself coalesces a boundary star; or
* that a trace comparison implies the required positive-operator bound.

The point-mass stopped profile in (5.6) passes structural orbit symmetry
before stopping and can coexist with good physical root loads supplied by
other rows. Its shell Dirichlet energy is order one, while the proposed
homogeneous capacity allowance is \(d^{-3}\). Hence BCAP, an equivalent
future-service star potential, or the explicitly priced excess (5.4) is a
genuine additional row.

Those exclusions are explicit in Sections 2, 4, and 5. The theorem proves
only the deterministic \(d^2\) aperture and the exact boundary-star
support.

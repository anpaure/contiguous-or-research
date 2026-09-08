# K17 GKS owner-exact state transversals and the complement-dual restriction

**Date:** 2026-08-01  
**Scope:** exact quotient-level changing-owner chronology on the authenticated
1,430-row GKS static flag system.  No upper-shadow, residence, deletion-spine,
voltage, or Hamilton claim is made.

## 1. Frozen input

The input is the authenticated switched GKS flag certificate

```text
scratch/threadA_k17_gks_dynamic_switched_seed2512_20260801.tsv
SHA256 908651cb50f5a6e8d8f9fead205d252ed67efc95c36a220ec4e052bb089b2451
```

and its exact phase-labelled turn catalogue

```text
scratch/threadA_k17_gks_dynamic_switched_seed2512_turns_20260801.tsv
SHA256 6b417b8413afb915ad03becec0154927f2a659642d26bfdae8bdd80eb909f7b9
```

The static packet-support relaxation has matching value 1,158.  That number
does **not** impose a common attachment state or distinct rank-9 owners, and is
not used as a physical certificate below.

## 2. Exact selected-state model

For packet (p), write

\[
Q_p=C^p_0\mathbin{\dot\cup}C^p_1\mathbin{\dot\cup}C^p_2,
\qquad |Q_p|=8.
\]

For each (a\notin Q_p), state (s=(p,a)) has rank-9 owner
(T_s=Q_p\cup\{a\}).  A **state transversal** is a choice (a_p) for every
packet such that the 1,430 necklace orbits
([Q_p\cup\{a_p\}]) are pairwise distinct.  Since the packet--owner incidence
graph is 9-regular on both sides, this is exactly an incidence perfect
matching.

Let `s=(p,a)`, `t=(q,b)`, and let `rho^delta` be a recorded cyclic
phase.  Put `D_i=rho^delta C_i^q` for `i=0,1,2` and
`D_3={rho^delta b}`.  There is a literal changing-owner arc `s->t`
with entering coordinate `beta` if and only if

\[
a\ne\beta,
\quad \rho^\delta(Q_q\cup\{b\})=Q_p\cup\{\beta\},                 \tag{2.1}
\]

\[
D_{i+1}\subseteq C_i^p\quad(0\le i\le2),                         \tag{2.2}
\]

and

\[
D_0=\{\beta\}\ \dot\cup\
\bigcup_{i=0}^{2}(C_i^p\setminus D_{i+1}).                        \tag{2.3}
\]

Conditions (2.1)--(2.3) are necessary and sufficient: (2.1) is the literal
Johnson owner update, (2.2) preserves the three surviving age classes, and
(2.3) is the exact refresh partition for the new age-zero class.

For a fixed state transversal, the maximum number of simultaneously usable
arcs is therefore the ordinary maximum matching of its induced directed
support, with one copy of the packet set on each shore.  This is an exact
fixed-transversal number, but maximizing it over all state transversals is a
strictly harder correlated problem.

## 3. Constructive owner-exact dynamic seed

The O3 H100 search changes a state transversal only along alternating cycles
of the 9-regular packet--owner incidence graph.  Consequently every
intermediate state has exactly one attachment per packet and exactly one per
owner orbit.  Each candidate is rescored by an exact Hopcroft--Karp matching
on the induced changing-owner graph.

The recorded natural `C3` transversal has:

```text
induced arcs                         2622
exact fixed-transversal matching     886
deficiency                            544
zero-out / zero-in packets          505 / 347
matched components                  1 cycle, 255 nontrivial paths, 289 isolates
```

The authenticated alternating-cycle seed `auth2514` has:

```text
induced arcs                         2292
exact fixed-transversal matching     988
deficiency                            442
zero-out / zero-in packets          378 / 413
matched components                  2 cycles, 274 nontrivial paths, 168 isolates
```

Thus the constructive correlated state choice improves the exact matched
support by 102.  The value 988 is **not claimed globally optimal**.  In
particular it is neither a cycle cover nor a Hamilton carrier.

The literal certificates are

```text
selected states
scratch/threadA_k17_gks_state_transversal_auth2514_20260801.tsv
SHA256 c17169a7a9bdf6bbcf96e8483270e08bba3f08b9391c2f365122f7525bfb7ede

matched phase-labelled arcs
scratch/threadA_k17_gks_state_transversal_auth2514_matched_20260801.tsv
SHA256 48169917696167c6c976b57a6ef396edc2b78d0b6f1b4ed535d7a38aacb792b7

H100 search audit
scratch/threadA_k17_gks_state_transversal_auth2514_search_20260801.audit.txt
SHA256 05d077f167e5a293a1d0751023c31ee5cd627b77dd1ee1d75652d6690f415856

independent literal replay
scratch/threadA_k17_gks_state_transversal_auth2514_replay_20260801.audit.json
SHA256 6b55505b9566a9b533e403430590f0d0469e127f04877b22f49c031fef16ba28
```

The independent replay reconstructs all arcs from (2.1)--(2.3), checks the
owner-orbit permutation, recomputes the exact fixed-transversal maximum
matching, and recomputes the path/cycle decomposition.

The proof-producing programs are

```text
scratch/search_threadA_k17_gks_state_transversal_20260801.cpp
SHA256 a541a0c2f2da83ef50db80831520588a97100ef1ae4540da3f6f2cd326e53d86

scratch/verify_threadA_k17_gks_state_transversal_20260801.py
SHA256 12e4b58c65456948db39761934c8d68950eaf1e5837f86bd37e7fed2bc53279a

scratch/audit_threadA_k17_gks_complement_dual_state_transversal_20260801.py
SHA256 5a02dd6de51cfb83a773a092300ff74281f85df07633da544b3a86e30851ec17
```

## 4. Exact complement-dual restriction

Fix a state transversal and let

\[
D:\{\text{rank-9 owner orbits}\}\longrightarrow
\{\text{rank-8 packet orbits}\}
\]

send the selected owner of packet (p) to (Q_p).  Let (C) denote
complementation and set

\[
H=C D^{-1} C,\qquad A=C D.
\]

Traversing the two incidence matchings from an owner through (D) and back
through (H^{-1}) forces the owner successor

\[
P=H^{-1}D=(C D C)D=(CD)^2=A^2.                                   \tag{4.1}
\]

Hence there is no successor choice left.  The dual union is a physical
changing-owner 2-factor precisely when every forced (A^2) successor satisfies
(2.1)--(2.3).  It is Hamilton only if, additionally, (A^2) is one cycle (and
the required lift voltage condition holds).

### Natural `C3` transversal

The forced permutation (A^2) has 146 cycles.  Exactly 421 of its 1,430
forced successors are legal changing-owner arcs and 1,009 are missing.  Every
legal forced arc has a unique phase label.  Missing sources by packet kind are

```text
pair_broken 230, pair_native 341, skip 277, triple 161.
```

Missing sources by static type id are

```text
0:135, 1:246, 2:7, 3:18, 4:16, 5:109, 6:124, 7:193, 8:161.
```

The certificate and replay are

```text
scratch/threadA_k17_gks_state_transversal_seed2512_natural_complement_dual_forced_20260801.tsv
SHA256 1d4a7a97e54616a01bfd7134bc3d1468760e7e9ef8b2e2cf5a445d0bb89eb908

scratch/threadA_k17_gks_state_transversal_seed2512_natural_complement_dual_20260801.audit.json
SHA256 8ff22f1e25d137da7ff3ff21c5db0a368a2bb91de5a0521c376f6e929b4de316
```

### Optimized `auth2514` transversal

Here (A^2) has 108 cycles.  Exactly 333 forced successors are legal and
1,097 are missing; again every legal one has a unique phase label.  Missing
sources by kind are

```text
pair_broken 231, pair_native 363, skip 261, triple 242.
```

The certificate and replay are

```text
scratch/threadA_k17_gks_state_transversal_auth2514_complement_dual_forced_20260801.tsv
SHA256 36f396bf4533753c3e432d13803097cf73cea4930498c334658ec22d259dff85

scratch/threadA_k17_gks_state_transversal_auth2514_complement_dual_20260801.audit.json
SHA256 3ca9e5f95357ac8fea6784c65d7d0fa5365c9a18bdf6b69ebb2017dc54c51ac8
```

Thus complement duality does not close either recorded state transversal.  It
is a scoped obstruction to those two transversals, not a theorem that no other
state transversal can satisfy the dual equations.

## 5. Exact remaining gate

The static GKS flag certificate is now accompanied by a literal, owner-exact,
phase-coherent dynamic path-forest seed of support 988.  The smallest remaining
unresolved object is an incidence-perfect state transversal whose induced
changing-owner graph has a cycle cover (and subsequently one cycle with unit
voltage).  The complement-dual restriction cannot supply that cover on either
the natural or `auth2514` transversal, so further alternating GKS containment
switches must be scored against the common-state cycle-cover constraints, not
only packet support or fixed-transversal matching size.

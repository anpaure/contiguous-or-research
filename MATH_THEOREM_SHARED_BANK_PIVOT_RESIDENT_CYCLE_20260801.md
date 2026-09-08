# A shared-bank pivot closes to a resident literal cycle with one owner

Date: 2026-08-01

Status: unconditional cyclic local construction.  It closes the clipped
residence runs only while the packet is retained as a cycle, or is opened at
the two global ends.  An internal opening still exports endpoint trace and
needs compatible host continuation.  Global owner-factor extraction, the
remaining upper palettes, and the occurrence-level compiler are not claimed.

## 1. Construction

Let `h>=2`, let `|B|=r-h`, and choose a nonempty pivot target
`X subseteq B` with two distinguished coordinates

\[
                         x_L,x_R\in X,\qquad x_L\ne x_R.
\]

Put `C=B-{x_L,x_R}`.  Choose mutually disjoint ordered banks outside `B`,

\[
 L=(\lambda_1,\ldots,\lambda_h),\quad
 R=(\rho_1,\ldots,\rho_h),\quad
 D=(d_1,\ldots,d_{h-1}),
\]

and one further coordinate `p`.  Thus the support has size

\[
                |B|+|L|+|R|+|D|+1=r+2h.                 \tag{1.1}
\]

Define

\[
 B^-=(B-\{x_R\})\cup\{p\},\qquad
 B^+=(B-\{x_L\})\cup\{p\},                             \tag{1.2}
\]

and

\[
\begin{aligned}
 L_t&=B^-\cup\lambda[1,t+1]\cup D[t+1,h-1],\\
 M_j&=B\cup\rho[1,j]\cup\lambda[j+1,h],\\
 R_t&=B^+\cup\rho[t+1,h]\cup D[1,t],
\end{aligned}                                            \tag{1.3}
\]

for `0<=t<h` and `0<=j<=h`.  Finally put

\[
                         H=B^-\cup D\cup\{\rho_h\}.       \tag{1.4}
\]

The cyclic owner order is

\[
 L_0,\ldots,L_{h-1},M_0,\ldots,M_h,
 R_0,\ldots,R_{h-1},H.                                  \tag{1.5}
\]

It has `3h+2` owners and the same number of cyclic transitions.

## 2. Owner, palette, and residence theorem

### Theorem 2.1

The sets in (1.5) are distinct rank-`r` owners forming a simple Johnson
cycle.  Its lower and upper transition colours are separately injective.
Every cyclic positive coordinate run has length at least `h+1`.

### Proof

All transitions in the old path are the shared-bank split-pivot transitions.
At the new end,

\[
 R_{h-1}\longrightarrow H
\]

exchanges `x_R` for `x_L`, and

\[
 H\longrightarrow L_0
\]

exchanges `rho_h` for `lambda_1`.  Hence every edge is Johnson.  The
distinguished signatures separate the five old edge classes.  The two new
lower colours are

\[
\begin{aligned}
 K_1&=C\cup\{p\}\cup D\cup\{\rho_h\},\\
 K_2&=B^-\cup D,
\end{aligned}                                            \tag{2.1}
\]

and the two new upper colours are

\[
\begin{aligned}
 V_1&=B\cup\{p\}\cup D\cup\{\rho_h\},\\
 V_2&=B^-\cup D\cup\{\rho_h,\lambda_1\}.
\end{aligned}                                            \tag{2.2}
\]

`K_1` has the new distinguished signature `(p)`.  `K_2` has the same
`(x_L,p)` signature as a left internal edge, but contains the complete `D`
bank, whereas every left internal colour replaces a nonempty initial part
of `D` by a `lambda` prefix.  Thus no collision occurs.  The same argument
separates `V_2` from the left internal upper colours using `rho_h`; `V_1`
has the seam signature `(x_L,x_R,p)` but differs from the two old seam
colours `B+p+L` and `B+p+R` by its nonempty `D` bank.  The remaining class
signatures differ.  This proves both palette injections and also proves that
`H` is a new owner.

For residence, every `lambda_j` and `rho_j` retains its old run of length
at least `h+1` (the `rho_h` run gains `H`).  Coordinates outside
`{x_L,x_R}` in `B` occur throughout.  The `x_L` and `x_R` runs have lengths
`2h+2` and `2h+1`, respectively.  Coordinate `p` has a cyclic run through
all right owners, `H`, and all left owners, of length `2h+1`.  Finally,
`d_i` occurs on

\[
 R_i,\ldots,R_{h-1},H,L_0,\ldots,L_{i-1},
\]

which has length

\[
                         (h-i)+1+i=h+1.                  \tag{2.3}
\]

These list every coordinate, proving cyclic residence.  \(\square\)

## 3. Exact cyclic source and pivot pin

The owner cycle is not merely factorable by the abstract residence
criterion.  It has the following explicit cyclic source of length `3h+2`:

\[
\begin{array}{l}
 C\cup\{p,d_1\},\ldots,C\cup\{p,d_{h-1}\},\\
 B^-,\\
 (B-\{x_R\})\cup\{\lambda_1\},\ldots,
 (B-\{x_R\})\cup\{\lambda_h\},\\
 X,\\
 (B-\{x_L\})\cup\{\rho_1\},\ldots,
 (B-\{x_L\})\cup\{\rho_h\},\\
 C\cup\{p,\rho_h\}.
\end{array}                                               \tag{3.1}
\]

### Theorem 3.1

The cyclic depth-`h` derivative of (3.1) is exactly (1.5).  Its cyclic
depth-`h-1` row consists of the literal owner intersections, and its cyclic
depth-`h+1` row consists of the literal owner unions.

Delete the displayed source letter `X` and open the cycle immediately
before the first `C+p+d_1` letter.  Reinsert `X` at the same internal cut.
Then every old linear interval transports with the same OR.  The cells of
source length at most `h` outside that transport image are exactly

\[
 X,\qquad B\cup\lambda[h-i+1,h],\qquad
 B\cup\rho[1,i],\quad1\le i<h.                           \tag{3.2}
\]

Thus the pivot singleton and both compiler rays are preserved in one
literal resident cyclic source.

### Proof

Sliding a length-`h+1` window through the first bank successively replaces
`d_i` by `lambda_i`, giving `L_0,...,L_(h-1)`.  The next `h+1` windows give
the central geodesic because `X` restores `x_R` on the left and `x_L` on
the right.  The rho bank gives `R_0,...,R_(h-1)`.  The last source letter,
followed cyclically by the complete `D` bank and `B^-`, gives `H`.  This
proves the owner row.

For adjacent windows, the common `h` source letters give their
intersection.  Equivalently, if `O_t` and `O_(t+1)` are consecutive owners
and `C_t` is their shared source block, then

\[
 O_t\cap O_{t+1}=C_t\cup(A_t\cap A_{t+h+1}).             \tag{3.3}
\]

On the old transitions, the extra endpoint intersection is already in
`C_t`, exactly as in the tight split source.  At `R_(h-1)->H` and
`H->L_0`, that endpoint intersection is `C`, which is also in the shared
block.  Hence all lower q1 cells are literal.  Upper q1 literalness is the
tautological union of the `h+2` spanning source letters.

The two old letters adjacent to `X` are

\[
 (B-\{x_R\})+\lambda_h,qquad
 (B-\{x_L\})+\rho_1.
\]

Their union contains `B` and hence `X`.  The monotone insertion criterion
therefore transports every old interval OR.  Direct one-sided unions from
`X` give (3.2).  \(\square\)

### Pin scope

The source (3.1) preserves the occurrence rows used by the pivot compiler:
the literal cell `X`, both rays, every owner, and both q1 palettes.  It does
not preserve the earlier presentation in which the surrounding `lambda_j`
and `rho_j` letters were singletons.  Those exact nine presentation pins
are incompatible with this fixed owner cycle; the core-bearing letters in
(3.1) are load-bearing.  This is harmless for the monotone insertion and
ray compiler, but any external guard that named the old singleton letters
must be regenerated against (3.1).

## 4. `k=17` witness

Take `r=9,h=3`,

\[
 B=\{0,1,2,3,4,5\},\quad X=\{0,1\},\quad
 L=\{6,7,8\},\quad R=\{9,10,11\},
\]

with `p=12` and `D={13,14}`.  The source cycle is

```text
12348 20540 4157 125 189 317 3 574 1086 2110 6204
```

and the owner cycle is

```text
28797 20733 4605 511 959 1855
3647 7742 15422 30782 30781
```

Independent O3 C++ replay verifies:

```text
11 distinct rank-9 owners in one Johnson cycle
11 distinct literal rank-8 q1 colours
11 distinct literal rank-10 q1 colours
minimum cyclic positive run 4
exact pivot cell X and four ray cells
exact linear old-deck transport after deleting/reinserting X
```

It also gives a useful negative calibration: all nine old surrounding
source-letter pins have zero feasible cyclic placement, while the exact
compiler pivot/ray pin has one.

Artifacts:

```text
scratch/audit_k17_compressed_pivot_cycle_20260801.cpp
65d088c920136291d4e43e61fccd0cc12f3543c4e24a0e85200afc43e7a15383

scratch/k17_compressed_pivot_cycle_20260801.audit.json
31b456f296fb3efac662b02fa35d6bcbce06c25ccc017f7e6ac3e38bef497f4c
```

## 5. Prospective extraction from the active `k=17` SCD factor

All eleven owners occur uniquely in the active SCD owner partition.  In
cycle order their physical locations are

```text
28797  c188:4       20733  c1716:0      4605   c188:2
511    c112:4       959    c330:5       1855   c5:0
3647   c23:1        7742   c323:4       15422  c561:5
30782  c634:6       30781  c954:5
```

Extracting each as a singleton requires twenty distinct base cuts.  Those
cuts kill twenty old lower-q1 and twenty old upper-q1 occurrences.  The
cycle internally recreates eight of the killed lower colours and six of the
killed upper colours.  The residual killed palettes are

```text
lower:
255 479 703 3615 4541 11326 12413 15390 28734 30749 30750 30773

upper:
1919 3711 5117 7806 8703 12797 15486
22781 29053 30846 30909 31294 66495 73278
```

Thus the cycle has a completely explicit prospective extraction macro, but
it is not an append-only free macro.  A global selector must provide other
occurrences or external providers for these twelve/fourteen casualties and
must avoid every claimed owner position.

Artifacts:

```text
scratch/k17_compressed_pivot_cycle_extraction_macro_20260801.tsv
20cc849eff92e1dc26ac4cb6c47ffc718a1a0deb81dd0613ffa741ea77b74693

scratch/audit_k17_compressed_pivot_cycle_extraction_20260801.cpp
f5d4a58c4a5e9648a945905694b24dbc4d9d72d937b33fc8c4d38f935336ea73

scratch/k17_compressed_pivot_cycle_extraction_20260801.audit.json
7e6fca9ba74eeaaacb0a254504d44d946cd202198cef39c1e590cb18727c6fc2
```

### 5.1 Safe J6 opening

Five cycle upper colours have an old SCD occurrence outside the twenty
macro cuts:

```text
3903  at 52:2       4607  at 157:1       20989 at 406:6
30783 at 1484:6     31806 at 46:7
```

Choose the edge `R_(h-1)->H`, whose upper colour is `30783`, and protect the
old boundary `1484:6` from being cut.  The resulting J6 owner path is

```text
30781 28797 20733 4605 511 959
1855 3647 7742 15422 30782
```

with endpoints `30781,30782`.  It delivers the ten upper colours

```text
30845 28925 20989 4607 1023
1983 3903 7743 15934 31806
```

and the ten lower colours

```text
28733 20605 4349 509 447
831 1599 3646 7230 14398.
```

The removed lower/upper pair is `30780/30783`; the upper colour survives at
the protected old edge.  Linear replay finds zero short positive run wholly
internal to the opened path.  This opening therefore removes the cycle
charge from the selector, but it is not boundary-state-free: every cut of
the cycle splits four nonconstant coordinate runs and creates six endpoint
fragments shorter than `h+1`.  Hence J6 needs compatible continuation at
both endpoints unless they become the two global ends.  It does not make the
fourteen/twelve extraction casualties disappear, and the old provider
`1484:6` must be an explicit conditional no-cut row of J6.

An independent replay verifies all cyclic identities and the exact pivot/ray
cells.  At the displayed cut before owner zero, its four split runs have
`(prefix,suffix)` lengths

```text
bit 0: (7,1)   bit 12: (3,4)   bit 13: (1,3)   bit 14: (2,2).
```

Artifacts:

```text
MATH_AUDIT_K17_SHARED_BANK_PIVOT_CYCLE_INDEPENDENT_20260801.md
e1b98374f726e85add9e228dfe030d4073ef6326e6c8cc1285c5a65a7cb94c7c

scratch/audit_k17_shared_bank_pivot_cycle_independent_20260801.cpp
4f6d50e398e0c0f8d5987c5bf7803915db6f4359e707fce09da16d83465c4efe

scratch/k17_shared_bank_pivot_cycle_independent_20260801.audit.json
c066f4529e3dd41a23bc0dca6462628a3acdb2dac716a2eec070a85aeee7feec
```

## 6. Scope

This theorem closes the packet's clipped residence state only in its cyclic
form.  The local object is a self-resident literal cycle with its own compiler
pins.  Any internal linear opening, including J6, exports endpoint trace and
requires host continuation, a splice, or explicit boundary handling.  The
theorem does not prove that the cycle can be extracted disjointly from a
chosen global owner factor while retaining every killed old palette
occurrence, nor does it cover ranks above `r+1` or solve the remaining common
cap.  Those are global correlated-selection gates, not local residence gates.

# Thread D: named-blocker witnesses and the K16 five-phase return graph

**Date:** 2026-07-30  
**Status:** exact one-cell and sharp-return censuses; no length-12,874 word is claimed

## 1. Current bracket and finite roots

The retained verified upper word is

```text
answers/k16_upper12875.word
length 12875
SHA-256 b02da0f2a669068d698ed30aaa2009daaf67d3badaa8c3321e6e245478318d79
```

and exhaustive literal replay covers all (2^{16}-1) nonempty masks.  The
counting lower bound is 12,873, so

\[
 12873\le \nu(16)\le12875.
\]

No single deletion of this word is universal.  Its four best two-hole
deletions and its one-hole terminal deletion are the coherent phase roots

\[
\begin{array}{c|c}
\text{deleted position}&\text{holes}\\ \hline
0&\{43117,44141\}\\
1&\{10349,11373\}\\
6435&\{20065,20067\}\\
12873&\{52833,52835\}\\
12874&\{10365\}.
\end{array}
\]

The corresponding literal words are retained as
`scratch/k16_delete12875_p{0,1,6435,12873,12874}_partial.word`.  A complete
arbitrary one-substitution census fails on every one of these five roots.
This does not exclude radius two or three.

## 2. Exact one-cell census lemma

Let (W=(W_0,\ldots,W_{n-1})) have sole hole (T), and replace (W_p=o)
by (x\ne0).  Every newly created (T)-interval contains (p), hence

\[
 x\subseteq T. \tag{2.1}
\]

Let (L_p) be the multiplicity-weighted suffix-OR states strictly left of
(p), together with the empty state, and define (R_p) analogously on the
right.  Then the complete multiplicity delta is

\[
 \Delta c(U)=
 -\!\sum_{\ell\in L_p,r\in R_p}
   m(\ell)m(r)[\ell\vee o\vee r=U]
 +\!\sum_{\ell\in L_p,r\in R_p}
   m(\ell)m(r)[\ell\vee x\vee r=U]. \tag{2.2}
\]

Thus scanning all (n(2^{|T|}-1)) position/submask pairs is a complete
one-substitution theorem.  Formula (2.2), not an additive unique-owner
proxy, was used for every census below.  The same argument applies after a
fixed portal, so the return scan is also complete.

## 3. The named-blocker lemma

Suppose a fixed portal \(\pi\) changes one cell (p), covers the sole hole
(h), and leaves a sole blocker (a).  For an auxiliary edit bundle (R),
write (W^{R,\pi}) for the simultaneous literal word.  If exact replay (or
an equivalent witness certificate) proves every target other than (a)
covered in (W^{R,\pi}), then

\[
 W^{R,\pi}\text{ is universal}
 \quad\Longleftrightarrow\quad
 c_{W^{R,\pi}}(a)>0. \tag{3.1}
\]

In particular, an (a)-witness in (W^R) that avoids (p) automatically
survives the portal.  Therefore a proof-safe sufficient construction is:

1. (R) preserves all old coverage except the designated hole (h);
2. (R) creates a second (a)-witness avoiding (p);
3. literal replay checks that the portal still has no counterterm outside
   \(\{h,a\}\).

The third condition is essential.  Merely increasing the marginal
multiplicity of (a) is not enough if (R) changes the portal's other
intervals.

## 4. Append-0200 blocker \(a=0xa879\)

Let

```text
B = scratch/k16_append0200_12874_onehole.word
SHA-256 aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18
```

Then (H(B)=\{h\}), where (h=10365=\mathtt{0x287d}).  The complete
3,282,870-assignment scan has 26,701 installers, none universal.  Minimum
collateral is one, attained by exactly 16 values at position 6440:

\[
 V_{16}=\{\mathtt{0x2004}\vee s:s\subseteq\mathtt{0x0069}\}. \tag{4.1}
\]

Each performs

\[
 \{\mathtt{0x287d}\}\longmapsto\{\mathtt{0xa879}\}. \tag{4.2}
\]

For every one of these 16 portal words, all 3,282,870 possible return
substitutions were scanned.  Each has 27,840 substitutions that cover
`0xa879`, but none is universal.  The minimum return simply edits position
6440 back and recreates `0x287d`; away from 6440 the minimum collateral is
two.  In total, 445,440 blocker-serving return rows were checked.

Consequently one auxiliary substitution cannot create a portal-surviving
second `0xa879` witness while preserving all coverage.  The named-witness
route requires at least two auxiliary edits, i.e. at least three changed
positions including the portal.

There is also a complete arbitrary-value CSP on the six observed phase
cells

\[
 \{0,1,6439,6440,6441,12873\}.
\]

The two fixed gaps have OR `0xffff`; only 17 targets remain nonpermanent and
they have 285 exact interval forms.  The retained CP-SAT model reports
`INFEASIBLE` in 0.13 seconds.  This is an exact finite-model obstruction for
that six-cell support, but no proof-log claim beyond the retained exact model
and solver replay is made.  A completion must recruit another cell or use a
different global chronology.

## 5. Five-phase blocker \(h=0x287d\)

The new one-hole root is

```text
F = scratch/k16_fivephase_rex_hole20067.word
length 12874
SHA-256 eef3555aa12675de8707de994d20300aaf8e96538b4691880810d84454fbb1b5
H(F) = {20067} = {0x4e63}.
```

The complete one-cell scan evaluates 3,282,870 assignments.  Exactly 26,916
install `0x4e63`; none is universal.  Minimum collateral is one, attained by
128 terminal values

\[
 V_{128}=\{\mathtt{0x0002}\vee s:s\subseteq\mathtt{0x4e61}\} \tag{5.1}
\]

at position 12873.  Every sharp portal performs

\[
 \{\mathtt{0x4e63}\}\longmapsto\{\mathtt{0x287d}\}. \tag{5.2}
\]

All 128 portal states were then audited independently.  For each state:

* 3,282,870 return assignments were evaluated;
* 26,783 cover `0x287d`;
* none is universal;
* minimum collateral remains one;
* every best off-terminal return is at position 6439 and transfers the hole
  to `0xa879` (16 values).

The batch comprises exactly
\(128\cdot3,282,870=420,207,360\) assignment evaluations.  It used one H100 CPU, 48.99
seconds, and 12,288 KiB maximum RSS.  Therefore one auxiliary edit cannot
create the required nonterminal `0x287d` witness.  The five-phase named
witness also needs at least two auxiliary edits.

## 6. Exact representative continuation and the first exterior escape

For the representative terminal phase `0x4e63`, the exact minimum route is

\[
 0x4e63\xrightarrow{p_{12873}}0x287d
 \xrightarrow{p_{6439}}0xa879.
\]

Changing the terminal value again moves the singleton back to `0x4e63`, so
the scalar labels alone form a shuttle.  In that translated physical state,
the best genuinely exterior return recruits position 6420 and moves

\[
 0x4e63\longmapsto\{1651,3699\}.
\]

An exact next-return scan finds no completion: the minimum row edits 6420
again and leaves one debt, while every return away from 6420 leaves at least
six.  Other exact off-portal rows move to the mixed pairs
`{20065,52833}`, `{52321,52833}`, or the familiar boundary pair
`{43117,44141}`.  These are candidate states, not no-goes for larger
simultaneous bundles.

## 7. A broader fixed-support run is UNKNOWN

An exact interval-form CP model allowed arbitrary nonzero values at

```text
0,1,2,5921,6420,6435,6439,6440,6441,12871,12872,12873
```

in the five-phase word.  It has 54 nonpermanent targets, 355 interval forms,
1,592 witness variables, and 29,197 guarded witness implications.  The
one-worker run reached its 240-second limit after 4,425,012 branches and
722,827 conflicts, with status `UNKNOWN`.  Peak RSS was 140,684 KiB.
This is neither SAT nor UNSAT and supplies no mathematical conclusion.

## 8. Sharp remaining construction

The finite target is no longer “reduce aggregate holes.”  It is one of the
following named reserve constructions:

1. in the append-0200 root, create a second `0xa879` witness that survives a
   (p_{6440}) portal;
2. in the five-phase root, create a nonterminal `0x287d` witness that survives
   a (p_{12873}) portal.

One auxiliary edit is exactly excluded in both cases.  The next model should
price two-edit final witness intervals for the named blocker, retain exact
nonblocker coverage guards, and replay the simultaneous portal plus reserve
bundle.  A positive word must still pass the independent 65,535-mask
verifier.

The source-bad interval geometry is already small.  After fixing a
representative sharp portal, the exact radius-two catalogues are

| portal word | blocker | intervals with at most two source-bad cells | avoiding portal | mandatory-support sets | max width |
|---|---:|---:|---:|---:|---:|
| append-0200 | 43129 | 26,767 | 26,761 | 25,092 | 4 |
| five-phase | 10365 | 26,784 | 26,782 | 25,108 | 6 |

For an interval (I) and blocker (T), its mandatory support is

\[
 M_T(I)=\{i\in I:W_i\not\subseteq T\}.
\]

Any two-edit blocker witness must contain (M_T(I)), so rows with
\(|M_T(I)|>2\) are impossible and the displayed catalogues are complete.
The exact pricing problem is: choose one surviving interval, assign its
edited cells so their OR with the fixed cells is exactly (T), and use any
remaining edit capacity to satisfy the private-target Hall rows.  Literal
replay supplies every missing-target cut.  This is the next proof-safe
two-witness model; it is much smaller than optimizing aggregate hole count.

## 9. Reproducible artifacts

Primary sources and outputs are:

```text
scratch/threadD_k16_onehole_substitution_exchange_census_20260730.cpp
  SHA bd2f27339416d0d5855fac6e371700c976c888f95ae7e0aa16192eadf602c14b
scratch/threadD_k16_twohole_return_substitution_census_20260730.cpp
  SHA fabfd2f115d66b57f04d5235b4614601d1bd23e78f08f9fc89fc034015c20d17
scratch/threadD_k16_fivephase_hole20067_onecell_census_20260730.audit.json
  SHA dc33f876461d8e5c064cec31ff1e1e89fce79610272920a3dd600dbee86b95fd
scratch/threadD_k16_fivephase_hole20067_all128_return_20260730.audit.json
  SHA 3c2b5d6fa1ae47ec6b9a723f4666fb892538f05af5c691fe11d026cc46f17c91
scratch/threadD_k16_fixed_phase_support_cpsat_20260730.py
  SHA 7ed097c16860c8259de3cb300238704976f093f807f5296a855ffbfd81b4a04c
scratch/threadD_k16_fivephase_support12_cpsat_20260730.audit.json
  SHA 499dd3619e84c5105e740f8be53f58c846c910fb6f72f1e88cd73ec4b2098829
scratch/search_k16_append0200_phase_collar_csp_20260730.py
  SHA e29dca66534bd81240fe22507569e07d203e5eaf1daa553bdc3b09e3e7a1bbff
scratch/k16_append0200_phase_collar_csp_20260730.audit.json
  SHA 20cbfa5ef4bfe51f288db864fcedb224bdff99ac12064ca49ab10d20f8fce069
```

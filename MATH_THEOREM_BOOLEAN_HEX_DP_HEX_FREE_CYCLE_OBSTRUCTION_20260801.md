# Delcourt--Postle can produce a near-perfect body with a cycle and no ternary-hex move

Date: 2026-08-01  
Status: exact configuration calculation and a sharp black-box obstruction.
It proves that an applicable-hex supply theorem is false for an arbitrary
Delcourt--Postle output, even when only one physical cycle remains.  A cycle
contraction theorem must therefore plant its hex phases jointly with the
body or use a larger exchange family.

## 0. Result

Let `H_m` be the ordered Boolean-diamond four-graph, with

\[
 D=m(m+1),\qquad N={2m\choose m-1}.
\]

Let `X_m` be the three-uniform configuration hypergraph on `E(H_m)` whose
configurations are the full old phases

\[
                         O=\{o_1,o_2,e\}                 \tag{0.1}
\]

of the Cartesian ternary-hex family in
`MATH_THEOREM_BOOLEAN_HEX_TERNARY_FOUR_RESOURCE_ABSORBER_20260801.md`.

### Theorem 0.1 (hex-free near forest)

For every fixed physical-cycle cutoff `g`, and all sufficiently large `m`,
there is a four-resource matching `M` of size `N-o(N)` which contains no
configuration of `X_m` and whose physical projection has no cycle of
length at most `g`.

After deleting one atom from each remaining physical cycle, it becomes a
physical linear forest of size `N-o(N)` which is still `X_m`-free.

### Theorem 0.2 (one protected cycle, still no move)

For every fixed `g` and all sufficiently large `m`, there is a
four-resource matching `M` of size `N-o(N)` whose physical projection is
the disjoint union of

* one prescribed directed four-cycle; and
* a physical linear forest,

and which contains no configuration of `X_m`.

In particular the unique physical cycle has no applicable ternary-hex
cycle-mode packet at all.

This does not say that a favourable Delcourt--Postle colour or a jointly
planted body cannot contain many packets.  It says the published theorem's
hypotheses and conclusion do not force even one.

## 1. The packet-configuration hypergraph is extremely sparse

Fix an oriented target atom

\[
 e=(L,L+a+d,L+d,L+a).
\]

Its displayed Cartesian fan is indexed by

\[
                         (b,c)\in L\times([2m]\setminus(L+a+d))
\]

and therefore has `(m-1)^2` configurations.

### Lemma 1.1 (exact degrees)

The configuration hypergraph `X_m` is regular and linear:

\[
              d_{X_m}(x)=(m-1)^2,\qquad
              \Delta_2(X_m)\le1.                         \tag{1.1}
\]

#### Proof

A target atom has `(m-1)^2` fan options.  Each old packet line is obtained
from each of its three atoms as the distinguished hole, so the target
description counts every configuration exactly three times.  The symmetric
group on the ground set acts transitively on oriented atoms and preserves
the displayed fan.  Double counting therefore gives degree `(m-1)^2`.

Two atoms in one old phase recover the packet.  If one is the target, its
lower and upper differences recover `b,c`.  If both are off atoms, their
two lower colours recover the common `(m-2)`-core and the coordinates
`a,c`, while their two upper colours recover `b,d`; the tail/head roles fix
the orientation.  Thus a pair lies in at most one configuration.  `square`

The scale in (1.1) is much smaller than the Delcourt--Postle allowance.
Indeed

\[
       \Delta(X_m)=O(D),\qquad \Delta_2(X_m)=1,           \tag{1.2}
\]

where a three-configuration system may have degree of order
`D^2/log D` and pair-codegree `D^(1-beta)` for fixed `beta>0`.

## 2. Proof of Theorem 0.1

Combine `X_m` with the fixed-`g` physical-cycle configuration system used
in the valid ordered-diamond Delcourt--Postle fallback.  The two systems'
degree and mixed-codegree bounds add.  Equation (1.2) is lower order than
the already verified physical-cycle bounds, so the same corollary colours
the host with

\[
                         D(1+D^{-\alpha_g})             \tag{2.1}
\]

conflict-free matchings.

The host has `ND` atoms.  Its largest colour class consequently has size

\[
                         N(1-D^{-\alpha_g})=N-o(N),      \tag{2.2}
\]

contains no old ternary-hex phase, and has physical girth greater than `g`.
Deleting one edge per remaining cycle costs at most `N/(g+1)`.  A slow
diagonal choice of `g` gives the claimed `N-o(N)` forest.  Deletion cannot
create a forbidden configuration.  `square`

## 3. A literal protected directed four-cycle

Choose an `(m-2)`-set `S` and four distinct coordinates `a,b,c,d` outside
it.  Put

\[
\begin{array}{ll}
 T_0=S+a+b,&T_1=S+b+c,\\
 T_2=S+c+d,&T_3=S+d+a.
\end{array}                                                \tag{3.1}
\]

The directed Johnson edges

\[
                         T_0T_1,T_1T_2,T_2T_3,T_3T_0       \tag{3.2}
\]

are four legal ordered diamonds.  Their lower colours are

\[
                         S+b,S+c,S+d,S+a,
\]

and their upper colours are

\[
              S+a+b+c,S+b+c+d,S+a+c+d,S+a+b+d,           \tag{3.3}
\]

all distinct.  Their tails and heads are also separately distinct.
Hence (3.2) is a four-resource matching whose physical projection is one
directed four-cycle; call it `C`.

No three atoms of `C` form a configuration of `X_m`: every old hex phase
has three physical edges on six distinct physical vertices, whereas any
three edges of (3.2) share physical endpoints.

## 4. Condition the conflict system on the protected cycle

Delete from the ordinary host both physical role copies of every `T_i` and
all outer resources used by `C`.  Thus any residual matching is physically
vertex-disjoint and four-resource disjoint from `C`.

Condition `X_m` on the decision that all four atoms of `C` are selected:

1. retain every three-configuration disjoint from `C`;
2. when a configuration contains exactly one atom of `C`, retain its other
   two atoms as a size-two forbidden configuration; and
3. when it contains exactly two atoms of `C`, delete its third atom from
   the host.

There is no configuration contained in `C`.  Linearity of `X_m` gives the
exact bounded perturbation:

* a residual atom has degree at most `4` in the new size-two conflict
  graph (one possible partner for each fixed cycle atom); and
* at most `binom(4,2)=6` residual atoms are deleted in step 3.

All Delcourt--Postle degrees and codegrees are therefore unchanged
asymptotically.  Add the residual fixed-`g` physical-cycle conflicts and
apply the same colouring theorem.  As in the protected-bank theorem,
deleting the `O(1)` resource set costs only `O(1)` in the selected-class
bound.  We obtain a residual matching `K` of size `N-o(N)` such that

\[
                             C\cup K                         \tag{4.1}
\]

contains no configuration of `X_m`.

The physical graph of `K` is disjoint from `C` and has no cycle of length
at most `g`.  Delete one atom from every remaining cycle of `K`, and take a
slow diagonal `g->infinity`.  The resulting `C union F` has size `N-o(N)`,
has exactly the one protected cycle `C`, and is `X_m`-free.  This proves
Theorem 0.2.  `square`

## 5. Consequence for the cycle-contraction programme

The ternary hex remains a valid and useful **planted** cycle actuator.  But
there is no theorem of the form

> every large Delcourt--Postle body, or every such body with a physical
> cycle, contains an applicable ternary hex.

Theorem 0.2 fails it already at one cycle.  Retaining all colour classes
does not alter this logical point: the Delcourt--Postle theorem also remains
valid after the old phases are explicitly declared forbidden.

The weakest viable positive target is therefore conditional and joint:

> choose the body together with a bank of full old phases, and prove that
> every nonterminal physical cycle is routed through the target edge of one
> planted phase while its two partner edges lie on reusable path components.

The fixed-bank theorem proves this joint conditioning for any bounded bank
when the packet vertices are isolated.  What is still missing for cycle
contraction is a **non-isolated endpoint linkage** which puts the target
edge on the intended cycle without losing the four-resource and downstream
guards.

## 6. Replay

Run

```text
python3 scratch/audit_boolean_hex_dp_hex_free_cycle_20260801.py
```

The replay enumerates the complete ordered-diamond host and the displayed
packet catalogue for `m=3,4`, checks (1.1), verifies the protected directed
four-cycle, and checks the conditioned size-two/singleton conflict bounds.

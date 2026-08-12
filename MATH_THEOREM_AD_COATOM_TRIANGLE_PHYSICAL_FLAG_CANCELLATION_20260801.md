# A three-packet coatom triangle cancels the complete nested lower flag physically

Date: 2026-08-01  
Status: exact algebraic/owner-disjoint serial trace identity, superseded for
strict-rainbow planting by
`MATH_THEOREM_AD_COATOM_TWISTED_CUBE_RAINBOW_FLAG_ABSORBER_20260801.md`.
The three packets preserve their local U1--U4 phase data and restore every
lower counter, but they repeat three cross-packet lower-q1 socket colours.
They therefore cannot coexist unchanged in a globally q1-injective bank.

## 0. Result and relation to the flag-lattice theorem

The saturated flag-action theorem in
`MATH_THEOREM_COATOM_FLAG_SIGNATURE_AND_PLUCKER_LATTICE_20260801.md`
already proves that the local lower action has no hidden congruence.  The
new point here is physical: the shortest nontrivial closed walk in that
action lattice can be realized by three simultaneous packet slots whose
literal owner sets are pairwise disjoint.

For every `d>=2`, take three canonical mixed-screen packets with ordered
active pairs

```text
                         (x,y), (y,z), (z,x).          (0.1)
```

They share their internal filler flag and their third active label, but
have private extreme fillers and one private active label apiece.  Toggling
the three packets serially gives


\[
             \Delta_q(x,y)+\Delta_q(y,z)+\Delta_q(z,x)=0
             \qquad(1\le q\le d).                    \tag{0.2}
\]

This is exact equality of **multiplicity counters**, not merely equality of
support.  Every packet separately is owner-, immediate-palette-,
upper-deck-, residence-, and simple-topology-exact.  Thus its local U1--U4
data remain phase-exact after each move.  At the end, every lower trace
counter through depth `d` is exactly its initial counter.  However the
three old packet banks already share three q1 colours, so this is not by
itself a strict-rainbow physical absorber.

Among pairwise-owner-disjoint canonical mixed-screen packets, three is
minimal, even if two proposed packets use different cores or opposite
internal filler orders.  Any inverse depth-two pair has the same four-mask
signed support, whose union is its central upper-screen owner.  Thus the two
literal packets collide, while using one slot twice merely restores the
original word.

## 1. One canonical packet

Use active roles `(e,a,b,c,delta,infinity)` and abbreviate

```text
Ad=e a delta,  Bd=e b delta,  Cd=e c delta,
ab=e a b,      bc=e b c,      ca=e c a,
Iab=infinity a b, Ibc=infinity b c, Ica=infinity c a,
Ia=infinity e a, Ib=infinity e b, Ic=infinity e c.
```

The old and new active paths are

```text
P = Iab Ib bc Cd Ic Ibc Ica Ia ca Ad Bd ab,
Q = Iab Ia ca Cd Ic Ica Ibc Ib bc Bd Ad ab.          (1.1)
```

Let

\[
 F=(f_0,f_1,\ldots,f_d,f_{d+1})                     \tag{1.2}
\]

and let `K` be a disjoint core.  Replace each active triple `V` by its
ordered coatom block

\[
 B(V)=\bigl(K\cup V\cup(F-\{f_i\})\bigr)_{i=0}^{d+1}.\tag{1.3}
\]

At active transitions `1,3,5,7`, insert the upper screen

\[
 K\cup(V_j\cup V_{j+1})\cup(F-\{f_0,f_{d+1}\});     \tag{1.4}
\]

at every other transition insert the lower screen

\[
 K\cup(V_j\cap V_{j+1})\cup F.                      \tag{1.5}
\]

Write `X(a,b|c)` and `Y(a,b|c)` for the expansions of `P` and `Q`.
They have rank

\[
                         r=|K|+d+4                  \tag{1.6}
\]

and length `12d+35`.  The authoritative mixed-screen theorem proves that
`X<->Y` is exact for U1--U4.

For a word `W`, define its depth-`q` lower trace counter by

\[
 \mathcal L_q(W)=
   \sum_{i=0}^{|W|-q-1}
       {\bf e}_{\,W_i\cap W_{i+1}\cap\cdots\cap W_{i+q}}.
                                                               \tag{1.7}
\]

This records occurrences with multiplicity.

## 2. Exact rank-one flag action

For `2<=q<=d`, put

\[
\begin{aligned}
 P_q&=\{f_1,\ldots,f_{d+1-q}\},\\
 S_q&=\{f_q,\ldots,f_d\},\\
 Z_{uv}(R)&=K\cup\{\mathord\infty,u,v\}\cup R.
\end{aligned}                                                   \tag{2.1}
\]

### Theorem 2.1 (one-packet counter identity)

With new-minus-old orientation,

\[
\begin{aligned}
 \Delta_q(a,b\mid c)
  &:={\cal L}_q(Y(a,b\mid c))-{\cal L}_q(X(a,b\mid c))\\
  &= {\bf e}_{Z_{ca}(P_q)}-{\bf e}_{Z_{cb}(P_q)}
    +{\bf e}_{Z_{cb}(S_q)}-{\bf e}_{Z_{ca}(S_q)}.    \tag{2.2}
\end{aligned}
\]

At depth one,

\[
                              \Delta_1=0.             \tag{2.3}
\]

#### Proof

A window in (1.7) has `q+1<=d+1` letters, whereas consecutive screens are
separated by a block of `d+2` letters.  It therefore crosses at most one
screen.

Windows contained in blocks cancel because `P,Q` use the same active
triples.  Windows through lower screens cancel with their common selected
lower colours.  At an upper screen, windows using block letters on both
sides depend only on the active edge intersection; for the four upper
transitions these intersections have the same multiset in `P,Q`.  Only the
two one-sided windows remain.

Their active endpoint table is

```text
profile P_q: old left  Ib,Cd,Ibc,Ia   new left  Ia,Cd,Ica,Ib
profile S_q: old right bc,Ic,Ica,ca   new right ca,Ic,Ibc,bc.   (2.4)
```

Thus the `P_q` row gains `Ica` and loses `Ibc`, while the `S_q` row gains
`Ibc` and loses `Ica`.  Restoring `K` and the filler profiles gives (2.2),
with coefficient one in every term.  At `q=1`, the two filler profiles meet
inside the exact immediate-palette identity, giving (2.3).  \(\square\)

Equivalently, define the pair-node potential

\[
 v_q(cu)={\bf e}_{Z_{cu}(P_q)}-{\bf e}_{Z_{cu}(S_q)}.\tag{2.5}
\]

Then

\[
                         \Delta_q(a,b\mid c)
                         =v_q(ca)-v_q(cb).             \tag{2.6}
\]

This is the short closed-walk form of the general flag/Pluecker lattice.

## 3. Literal owner-disjoint triangle

Fix common, mutually distinct labels

\[
 K,\quad \mathord\infty,c,\delta,x,y,z,
       \quad f_1,\ldots,f_d.                          \tag{3.1}
\]

For packet `i=0,1,2`, choose private labels

\[
                         e_i,\ell_i,r_i               \tag{3.2}
\]

and use the filler order

\[
                         F_i=(\ell_i,f_1,\ldots,f_d,r_i).\tag{3.3}
\]

Use the roles

\[
 (a_0,b_0)=(x,y),\qquad
 (a_1,b_1)=(y,z),\qquad
 (a_2,b_2)=(z,x),                                    \tag{3.4}
\]

with common `c,delta,infinity` and private `e_i`.

### Lemma 3.1 (physical disjointness)

The complete owner sets of the three expanded packets are pairwise
disjoint, in both phases.

#### Proof

Every block owner contains at least one of its private extreme fillers:
omitting `ell_i` retains `r_i`, omitting `r_i` retains `ell_i`, and omitting
an internal filler retains both.  Every lower screen contains both private
extremes.  Hence blocks and lower screens belonging to different packets
cannot coincide.

Three of the four upper screens contain the private label `e_i`.  The sole
upper screen without it is

\[
 K\cup\{\mathord\infty,c,a_i,b_i\}
       \cup\{f_1,\ldots,f_d\}.                       \tag{3.5}
\]

For the three packets, its active pair is respectively
`{x,y},{y,z},{z,x}`, so these three owners are distinct.  Upper screens
also cannot equal blocks or lower screens because they contain neither
private extreme filler.  Within one packet, simplicity is Theorem 3.1 of
the authoritative mixed-screen construction.  \(\square\)

The construction uses exactly `r+11` distinct coordinates.  It therefore
fits in a `2r`-coordinate middle-layer ground whenever

\[
                         r\ge \max\{d+4,11\}.          \tag{3.6}
\]

### Theorem 3.2 (triangle cancellation)

For every `1<=q<=d`,

\[
 \Delta_q(x,y\mid c)+\Delta_q(y,z\mid c)
                         +\Delta_q(z,x\mid c)=0.       \tag{3.7}
\]

#### Proof

Depth one is (2.3).  At every other depth, substitute (2.6):

\[
 [v_q(cx)-v_q(cy)]+[v_q(cy)-v_q(cz)]
                       +[v_q(cz)-v_q(cx)]=0.           \tag{3.8}
\]

The cancellation is coefficientwise, hence is exact as an integer
occurrence counter.  \(\square\)

More precisely, the six noncommon occurrences migrate in two opposite
directed triangles at every depth:

```text
P_q profile:  Z_cx : packet zx -> xy
              Z_cy : packet xy -> yz
              Z_cz : packet yz -> zx

S_q profile:  Z_cx : packet xy -> zx
              Z_cy : packet yz -> xy
              Z_cz : packet zx -> yz.                (3.9)
```

Thus the same two occurrence permutations act synchronously on the entire
nested flag `q=2,...,d`; the depth changes the filler set but not the packet
transport.  This is the exact finite interface that a compiler-address
transport must respect.

The same shared pair nodes cause the physical defect.  The lower-q1 socket
colours

\[
 K\mathord\infty cx\{f_1,\ldots,f_d\},\quad
 K\mathord\infty cy\{f_1,\ldots,f_d\},\quad
 K\mathord\infty cz\{f_1,\ldots,f_d\}                 \tag{3.10}
\]

each occur in two packet palettes.  Hence the three packets are owner-
disjoint but not lower-q1-palette-disjoint.

## 4. Serial composition in one literal carrier

### Theorem 4.1 (prepared-slot serial absorber)

Let a simple carrier word contain three pairwise disjoint intervals equal
to the old words in Section 3.  Assume their common endpoints have the
displayed exterior attachments.  Replace the three intervals, in any
order, by their new phases.  Then:

1. every intermediate word preserves each packet's local U1--U4 phase data;
2. every intermediate word has exactly the same owner set as the initial
   word;
3. all exterior connector steps and clipped residence states are unchanged;
4. and the terminal word satisfies

   \[
                  {\cal L}_q(W_{final})
                    ={\cal L}_q(W_{initial})
                    \qquad(1\le q\le d).              \tag{4.1}
   \]

#### Proof

Each local move preserves its owner multiset, endpoints, immediate palettes,
compressed prefix/suffix and internal OR decks, and residence state.  Its
replacement is a simple Johnson path.  These statements are invariant under
relabeling, so they apply to all three intervals and compose serially.

For (4.1), a depth-`q` window fully inside a changed interval contributes
the local counter delta (2.2).  A window crossing an interval boundary is
unchanged: the first and last `d+2` block letters of the two phases agree
literally, while `q<=d`.  Thus the global counter change is the sum of the
three local changes, which vanishes by (3.7).  \(\square\)

This is a genuine replacement absorber: the three toggles change three
literal intervals, rather than appending `Theta(d)` repair letters.  The
only carrier boundary is the constant set of six fixed slot endpoints.
It is not a globally q1-rainbow prepared bank because of (3.10).

### Corollary 4.2 (exact address-transport sufficiency)

Let `Gamma_old,Gamma_new` be the occurrence-to-cell incidence graphs of a
fixed compiler before and after the three toggles.  Suppose a permutation
of compiler cells, fixing every cell outside the three packet banks, extends
the occurrence transport (3.9) to a bipartite-graph isomorphism

\[
                         \Gamma_{old}\cong\Gamma_{new}.         \tag{4.2}
\]

Then every old compiler matching transports to a new one, with no added
cell and no new Hall test.

#### Proof

Apply the incidence-graph isomorphism to every edge of the old matching.
It preserves both endpoints and disjointness, so the image is a matching of
the same cardinality covering the transported occurrences.  Outside the
packet banks it is literally unchanged.  \(\square\)

Condition (4.2) is sufficient, not asserted automatic.  In particular,
equality of the unaddressed counters (4.1) does not imply it.

## 5. Sharp two-packet obstruction

### Proposition 5.1

For `d>=2`, no nontrivial owner-disjoint absorber using one or two canonical
mixed-screen packets restores every lower counter.  This remains true if
the two packets use different filler orders.  Hence the triangle is the
shortest nontrivial owner-disjoint canonical absorber.

#### Proof

One packet has four distinct signed depth-two atoms and is nonzero.  If two
packets cancel, their depth-two signed supports agree with opposite signs.
For any canonical packet, let `G={g_1,...,g_d}` be its internal filler set,
in its chosen order.  At depth two its two profiles are

\[
 P_2=G-\{g_d\},\qquad S_2=G-\{g_1\}.                 \tag{5.1}
\]

The union of the four masks in the signed support is therefore

\[
 K\cup\{\mathord\infty,c,a,b\}\cup(P_2\cup S_2)
   =K\cup\{\mathord\infty,c,a,b\}\cup G.             \tag{5.2}
\]

But (5.2) is exactly the packet's sole upper-screen owner not containing
`e`.  Opposite signed supports have the same union, even when obtained by
reversing the filler order or by a different literal decomposition.
Therefore the two packets share a physical owner and cannot occupy distinct
slots of a simple carrier.  If the inverse move is instead applied to the
same slot, it returns that slot to its initial word and is the trivial
backtrack.  The triangle in (3.4) realizes the first possible nontrivial
owner-disjoint cancellation.  \(\square\)

This is an abelian cycle relation, not a noncommutative group commutator.
The three disjoint toggles themselves generate a cube `(Z/2Z)^3`; the useful
identity is the zero boundary of a triangle in the lower-counter module.

## 6. Exact remaining boundary

The theorem closes the requested **unaddressed nested-chain cancellation**:
all lower target values and multiplicities through depth `d` return exactly,
while each packet's U1--U4 phase invariants remain exact throughout.  It
does not close their cross-packet q1 resource conflict; the twisted-cube
theorem is the corrected rainbow-compatible construction.

It does not close either of the following.

1. **Prepared-slot reachability.**  A fixed literal old word has fibre one.
   The theorem does not prove that an arbitrary safe carrier contains the
   three required old intervals with a common internal filler flag and safe
   exterior attachments.  It proves that, once planted, they are mutually
   physically compatible.
2. **Nonlinear compiler U5.**  A compiler uses occurrence addresses and
   interval-survival/nonzeroness constraints, not only the value counter
   `L_q`.  The three packets occur at different word positions, so (3.7)
   does not identify their address-labelled cells.  One final common-cap
   Hall matching, or a synchronized address transport theorem, is still
   required.

Thus the saturated flag lattice plus the triangle remove both the algebraic
and mutual-owner-collision objections.  The sharp remaining gate is global
physical planting coupled to the terminal compiler.

## 7. Independent replay

The dependency-free audit constructs the three literal packets for every
`1<=d<=12`; verifies ranks, Johnson adjacency, simple/equal owner sets,
pairwise owner disjointness, U1--U4, the exact formula (2.2), and the
coefficientwise cancellation (3.7):

```text
scratch/audit_ad_coatom_triangle_lower_chain_absorber_20260801.py
scratch/ad_coatom_triangle_lower_chain_absorber_20260801.audit.json
```

It reports

```text
PASS_AD_COATOM_TRIANGLE_LOWER_CHAIN_ABSORBER
```

with canonical payload SHA-256

```text
6aa502d0d3fc9de4d7a2ca981cc54c0bc302cf8754228174f51d2dff81cdcadf
```

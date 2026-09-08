# A Boolean-diamond C6 repairs one lower--upper pair while preserving directed ports and a rainbow opening

Date: 2026-08-01  
Lane: H2, Delcourt--Postle cover-down / bounded Boolean absorber  
Status: unconditional local identity and exact conditional `O(1)` cover-down

## 0. Result and scope

The valid Delcourt--Postle theorem supplies an `N-o(N)` matching in the
ordered four-resource Boolean-diamond host.  It does not align the remaining
lower and upper colours with a bounded absorber bank.  This note isolates an
exact bounded interface which would do so.

There is a six-owner alternating `C6` with the following simultaneous
properties.

1. Its off-to-on switch replaces two atoms by three and consumes exactly one
   aligned legal target atom: one missing lower colour, one containing
   missing upper colour, one unused tail, and one unused head.
2. Every intermediate state respects tail and head capacity one.
3. There is a unique pairing of three complementary directed rails for which
   both full phases are one directed cycle.  Opening the same untouched rail
   edge makes both phases directed spanning paths with the same opening
   endpoints.
4. The two full phases use the same lower and upper colour multisets.  Hence a
   literal q1-rainbow factor/opening certificate is transported, rather than
   merely its scalar endpoint ledger.

Consequently, if all but `C` pairs in the Delcourt--Postle leave admit
pairwise compatible installed copies of this six-socket record, then the
matching covers all but `C` lower and `C` upper colours.  On the normalized
fixed-`Q` capacity-slot host the residual typed leave is exactly

```text
                         (C,C,2C).
```

An ordinary Hall criterion is exact on the selector-separable face defined
below.  The separability, rail, graphic, and sidecar hypotheses are premises;
none follows from `N-o(N)` alone.  Thus this is not an unconditional
`B(k)+O(1)` theorem.  In particular, a bounded number of unresolved resource
quartets need not have bounded literal compiler weight without a separate
regeneration theorem.

No Joos--Mubayi--Smith exact matching theorem is used.

## 1. The ordered four-resource host

Fix owner rank `m`.  The four shores are

\[
 {\cal L}={ [2m]\choose m-1},\qquad
 {\cal U}={ [2m]\choose m+1},\qquad
 {\cal T},{\cal H}\cong { [2m]\choose m}.
\]

The last two are distinct tail and head copies.  For `L` of rank `m-1` and
distinct `x,y` outside `L`, write

\[
 [L;x,y]=\{L,L+x+y,(L+x)_{\rm tail},(L+y)_{\rm head}\}.       \tag{1.1}
\]

Its physical projection is the directed Johnson edge

\[
                         L+x\longrightarrow L+y.                \tag{1.2}
\]

A host matching therefore has distinct lower colours, distinct upper
colours, outdegree at most one, and indegree at most one.  The valid
Delcourt--Postle result gives a directed linear forest with `N-o(N)` atoms,
where `N=binom(2m,m-1)`.

The same formulas apply to the fixed-`Q` capacity-slot host after choosing
one literal outgoing and one literal incoming slot at every named owner.  In
that use, every displayed slot is required to survive the puncture and the
affine slot baseline is removed before the leave is counted.

## 2. The six-owner directed diamond

Let `K` have size `m-2`, and choose four distinct labels `a,b,c,s` outside
`K`.  Put

\[
 D_x=K+x,
\]

\[
 U_{abs}=K+a+b+s,\quad U_{acs}=K+a+c+s,\quad
 U_{bcs}=K+b+c+s,                                      \tag{2.1}
\]

and name the six owners

\[
 A_1=X_{ab},\quad A_2=X_{ac},\quad A_3=X_{bc},\qquad
 B_1=X_{as},\quad B_2=X_{bs},\quad B_3=X_{cs},           \tag{2.2}
\]

where `X_uv=K+u+v`.  Every `A_i` will be used as a tail and every `B_j` as a
head.

Define the old phase

\[
\begin{array}{lll}
 e_a=(D_a,U_{acs};A_2\to B_1),&
 e_b=(D_b,U_{abs};A_1\to B_2),&
 e_c=(D_c,U_{bcs};A_3\to B_3),
\end{array}                                                   \tag{2.3}
\]

and the new phase

\[
\begin{array}{lll}
 f_a=(D_a,U_{abs};A_1\to B_1),&
 f_b=(D_b,U_{bcs};A_3\to B_2),&
 f_c=(D_c,U_{acs};A_2\to B_3).
\end{array}                                                   \tag{2.4}
\]

Here `(D,U;X->Y)` denotes the atom using lower resource `D`, upper resource
`U`, tail `X`, and head `Y`.

### Theorem 2.1 (directed four-resource equality)

Both (2.3) and (2.4) are host matchings and

\[
                  e_a+e_b+e_c=f_a+f_b+f_c                 \tag{2.5}
\]

as multisets separately on all four shores.  In particular both phases use

\[
 \{D_a,D_b,D_c\},\quad
 \{U_{abs},U_{acs},U_{bcs}\},\quad
 \{A_1,A_2,A_3\}_{\rm tail},\quad
 \{B_1,B_2,B_3\}_{\rm head}.                              \tag{2.6}
\]

If `e_b` is the target, then

\[
 R=\{e_a,e_c\},\qquad A=\{f_a,f_b,f_c\}                  \tag{2.7}
\]

satisfy

\[
                    \operatorname{res}(A)
       =\operatorname{res}(R)\mathbin{\dot\cup}
        \operatorname{res}(e_b).                           \tag{2.8}
\]

Thus `R->A` simultaneously repairs exactly one missing lower colour and one
missing upper colour and consumes exactly the target tail and target head.

#### Proof

Every containment in (2.3)--(2.4) is immediate from (2.1).  Reading the
four columns gives (2.6), hence (2.5).  The off pair uses neither `D_b`,
`U_abs`, `A_1`, nor `B_2`; subtracting `e_b` from (2.5) proves (2.8).
\(\square\)

The union of the two phases is the alternating directed-socket `C6`

```text
A1--e_b--B2--f_b--A3--e_c--B3--f_c--A2--e_a--B1--f_a--A1.
```

One literal matching-safe serialization is

```text
remove e_a, add f_a, remove e_c, add f_b, add f_c.          (2.9)
```

After every operation, no tail or head is repeated.  The temporary loss of
one atom is harmless for a terminal cover-down; a prefixwise compiler would
need to declare these five microstates legal.

## 3. The unique three-rail opening wrapper

The preceding identity carries palettes and capacities, but a physical
factor/opening record also needs topology.  Suppose three internally
vertex-disjoint directed paths have endpoint pairing

\[
 P_1:B_1\leadsto A_3,\qquad
 P_2:B_2\leadsto A_2,\qquad
 P_3:B_3\leadsto A_1.                                  \tag{3.1}
\]

Their internal vertices avoid the six sockets.  Let `P=P_1 union P_2 union
P_3`.

### Theorem 3.1 (simultaneous cycle and common opening)

Both

\[
 C_{old}=P\cup\{e_a,e_b,e_c\},\qquad
 C_{new}=P\cup\{f_a,f_b,f_c\}                           \tag{3.2}
\]

are one directed cycle on the same vertex set.  If `g` is any edge internal
to one of the three rails, then `C_old-g` and `C_new-g` are directed spanning
paths with the same two opening endpoints.

If the rail q1 colours are distinct and disjoint from the three phase lower
colours, then `C_old` is q1-rainbow if and only if `C_new` is q1-rainbow.
The analogous statement holds for the upper palette.  Hence the same
occurrence-labelled opening edge `g`, not only the same scalar boundary
type, is transported by the switch.

If, in addition, the two cycles in (3.2) are spanning q1-rainbow Hamilton
cycles, and the common opening edge has q1 colour `Q`, each opened Hamilton
path has sole q1 hole `Q`, and both of its endpoints contain `Q`.  Thus both
carry the literal `B1` opening state `(z,l,r,b)=(0,0,0,1)`.

Moreover, among the six possible bijections from the `B` sockets to the `A`
sockets, (3.1) is the unique one for which both full phases are a single
cycle.

#### Proof

The old cycle has the directed order

\[
 A_1\xrightarrow{e_b}B_2\xrightarrow{P_2}A_2
 \xrightarrow{e_a}B_1\xrightarrow{P_1}A_3
 \xrightarrow{e_c}B_3\xrightarrow{P_3}A_1.              \tag{3.3}
\]

The new cycle has the directed order

\[
 A_1\xrightarrow{f_a}B_1\xrightarrow{P_1}A_3
 \xrightarrow{f_b}B_2\xrightarrow{P_2}A_2
 \xrightarrow{f_c}B_3\xrightarrow{P_3}A_1.              \tag{3.4}
\]

Deleting a common rail edge opens either cycle at the same physical edge.
Theorem 2.1 gives equality of both phase palettes, while the rails are fixed.

For uniqueness, identify the old and new `A->B` matchings with
`alpha=(12)` and `beta=(23)`.  A rail pairing `tau:B->A` gives component
permutations `tau alpha` and `tau beta`.  Directly checking `S_3`, both are
3-cycles only for `tau=(13)`, which is exactly (3.1).  \(\square\)

### Corollary 3.2 (the target gap is a graphic-safe ear)

With the common opening edge `g` withheld, the off state

\[
                       (P-g)\cup\{e_a,e_c\}              \tag{3.5}
\]

is a two-path forest.  Adding the target `e_b` gives the old opened path;
switching the off pair to the new phase gives the new opened path.  Thus the
gain-one switch merges exactly two local path components and creates no
cycle.

This corollary is literal only when the rails exist with the occurrence
labels and disjointness stated above.  An abstract contracted pairing does
not imply a Boolean/q1-distinct rail realization.

The off state (3.5) itself is not `B1`: it has both the target cut and the
common rail cut.  The preserved sidecar is the **virtual full phase**
`C_old-g` before activation and the actual full phase `C_new-g` after
activation.  Equivalently, one may consume the old target opening and reopen
at `g`.  Confusing the two-cut off state with either full opened phase would
be an edge-count error.

## 4. A serial cover-down theorem

Let `M` be a directed linear-forest host matching of size `N-h`.  Its missing
lower and upper shores both have size `h`.  A **partial target record** is a
matching `J={t_1,...,t_r}` of legal atoms, disjoint from `M`, whose lower and
upper resources are distinct subsets of those two missing shores.  Every
target therefore has a declared unused tail and head.  Put

\[
                              c=h-r.                       \tag{4.0}
\]

Fix, if needed, a protected physical scaffold `F_fix` such that
`F_fix union phi(M)` is a forest; take `F_fix` empty otherwise.

For `i<=r`, a **serial transparent packet record** consists of:

1. a suspended-hex off pair `R_i subset M` and on triple `A_i`, with target
   `t_i` and identity (2.8);
2. literal resource privacy from every other selected record;
3. graphic safety after contracting
   `F_fix union phi(M_(i-1)-R_i)`, equivalently independence of the three new
   projected edges in that quotient; and
4. a separate occurrence-labelled sidecar state `Sigma_(i-1)` and a state
   `Sigma_i` obtained by replacing its designated full old phase by the full
   new phase, together with either the explicit rail/opening wrapper of
   Theorem 3.1 or another literal certificate that both states have the
   required q1 factor/opening property.

Here

\[
 M_0=M,\qquad M_i=(M_{i-1}-R_i)\cup A_i.                  \tag{4.1}
\]

The records are ordered because graphic safety and factor topology need not
compose from packetwise tests made only in the initial graph.  The initial
sidecar state `Sigma_0` is part of the hypothesis; preservation does not
create one.

### Theorem 4.1 (exact bounded-leave cover-down)

If `M,J` admit serial transparent packet records for all `t_1,...,t_r`, then

\[
 M^+=\left(M-\bigcup_{i=1}^{r}R_i\right)
          \cup\bigcup_{i=1}^{r}A_i                      \tag{4.2}
\]

is a directed physical linear forest of size `N-c`.  It has exactly `c`
missing lower colours and `c` missing upper colours, respects every tail and
head capacity, and transports the separately declared literal q1
factor/opening sidecar through `Sigma_0,...,Sigma_r`.

On the normalized fixed-`Q` host, if the initial typed leave is
`(h,h,2h)`, the final typed leave is exactly `(c,c,2c)`.

#### Proof

By (2.8), one packet adds precisely the four resources of its target and
gains one atom.  Resource privacy lets the identities add, so

\[
 |M^+|=N-h-2r+3r=N-c.                                    \tag{4.3}
\]

The selected targets have distinct missing lower and upper resources and
distinct declared tail/head resources.  Hence exactly `c` lower and `c`
upper colours remain uncovered and no capacity is exceeded.  In the
normalized fixed-`Q` host, each
processed target removes one resource from each outer shore and two from the
slot shore, proving `(c,c,2c)`.

Apply the records in their declared order.  The quotient graphic test makes
each expansion acyclic.  For a rail record, Corollary 3.2 is the local
version of the same statement.  The four-resource virtual completion

\[
       \widehat M_i=M_i\cup\{t_j:i<j\le r\}               \tag{4.4}
\]

is useful only for the resource ledger: `\widehat M_(i-1)` contains the full
old phase `R_i union {t_i}` and `\widehat M_i` contains the full new phase
`A_i`.  It is not, by cardinality alone, the odd-ground q1 factor sidecar.
Its constant size is `N-c`, not necessarily `N`.
Theorem 2.1 preserves both palettes and all tail/head degrees in the
four-resource host.  Separately, row 4 transports the declared sidecar
`Sigma_(i-1)` to `Sigma_i`.  Induction proves both assertions without
identifying these two objects. \(\square\)

The theorem uses a six-atom local circuit, but it does not assert that the
support of every packet, including its complementary rails, has bounded
length.  The bounded object is the six-socket interface.

## 5. The exact Hall reduction on a selector-separable bank

The remaining correlation can be exposed as an ordinary Hall cut on one
strong but useful face.

Let `L_0,U_0` be the two missing outer shores, both of order `h`.  A
**selector-separable packet graph** is a bipartite graph `B` on
`L_0 union U_0` with one verified serial packet record for every edge, such
that one fixed total order is declared on its edges and, for **every** graph
matching `K subseteq E(B)`, the records indexed by `K`, in the inherited
order,

* have disjoint off envelopes and distinct fresh tail/head ports;
* avoid the fixed body and every unselected private envelope, including all
  rail, cut-edge, and opening-occurrence supports carried by the records;
* lie in one fixed quotient forest, or carry a common increasing component
  potential which proves the current-state graphic tests after each `R_i` is
  removed; and
* admit one initial sidecar `Sigma_0` and occurrence-labelled transparent
  transitions which compose in the inherited order.

This is substantially stronger than saying that every pair has some
absorber.  In particular, the corridor or off phase is not allowed to depend
on a later selector in a way that creates hidden three-dimensional
conflicts.

### Theorem 5.1 (Hall deficiency equals residual pair debt in the bank)

Put

\[
 \delta(B)=\max_{X\subseteq L_0}\bigl(|X|-|N_B(X)|\bigr). \tag{5.1}
\]

On a selector-separable packet graph, the smallest number of lower--upper
pairs left unresolved **relative to this declared packet bank** is exactly
`delta(B)`.  In
particular,

\[
                         \delta(B)\le C                   \tag{5.2}

is sufficient for the conclusion of Theorem 4.1 with `c<=C`.

#### Proof

The deficiency form of Hall's theorem gives a graph matching of size
`h-delta(B)`, and no larger matching exists.  Selector separability lifts
every graph matching to a partial target record with mutually compatible
packet records; Theorem 4.1 then applies.  Conversely, every lifted packet
uses a distinct lower and a distinct upper resource, so its selectors
project to a graph matching.
\(\square\)

For a bounded constant `C`, (5.2) is the promised specialized cover-down
cut.  Proving it for the leave of some Delcourt--Postle colour, together with
the separability rows, is still open.

## 6. Why this does not follow from Delcourt--Postle alone

The following exact obstructions prevent an unconditional conclusion.

1. A protected reserve may be deleted before Delcourt--Postle, but that only
   proves coexistence.  It does not make the eventual leave equal to the
   target resources of the reserve.
2. One suspended `C6` repairs a complete Boolean atom, so its missing lower
   and upper colours must satisfy `L subset U`.  An arbitrary lower--upper
   pair in a Delcourt--Postle leave need not be comparable; this is already
   an absent edge in the compatibility graph of Section 5.
3. Count-neutral Boolean circuits preserve both outer leave sets.  They can
   move slot pairings but cannot manufacture a missing lower--upper target.
4. Every canonical suspended-hex catalogue through one target has a small
   owner transversal, so quadratic raw multiplicity does not imply a private
   selector-separable bank.
5. Individual graphic safety does not compose; the selected quotient edges
   can close a cycle.  Likewise, endpoint counts do not certify a literal
   q1 opening.  The unique rail permutation in Theorem 3.1 is extra
   occurrence-level data.
6. Literal fixed-`Q` small cases contain capacity/Hall deficiencies, and a
   full Delcourt--Postle colouring can have locked terminal exchange
   components.  The near-matching theorem therefore has no hidden exact
   cover-down corollary.

Thus the exact remaining all-dimension statement is:

> choose a Delcourt--Postle body and a selector-separable installed packet
> bank jointly so that (5.2) has absolute deficiency, the quotient edges are
> graphic-independent, the unique rail/opening records compose, and the
> `c` residual quartets have bounded literal regeneration/compiler weight.

## 7. Audit

The independent finite-pattern replay is

```text
scratch/audit_h2_boolean_diamond_c6_tail_head_sidecar_coverdown_20260801.py
```

It checks, for owner ranks `3,...,12`, every rank and containment, the four
typed phase equality, the target-gain identity, all five matching-safe
microstates, the alternating `C6`, all six rail permutations and uniqueness
of `tau=(13)`, both directed cycles, the common opened paths, and the
two-path off state.  It also exhausts every bipartite graph of order at most
four per shore and verifies

\[
 h-\nu(B)=\max_X(|X|-|N_B(X)|),                           \tag{7.1}
\]

as well as the cover-down arithmetic.

The audit is a proof replay of the finite interface.  It does not enumerate
Delcourt--Postle colour classes, construct the complementary rails, prove
selector separability, or certify a downstream common-cap compiler.

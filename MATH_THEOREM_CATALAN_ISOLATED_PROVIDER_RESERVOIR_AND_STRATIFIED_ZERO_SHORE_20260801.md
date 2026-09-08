# A Catalan isolated-provider reservoir preserves the odd host, but a bounded
# number of mixed-head strata has a macroscopic zero shore

Date: 2026-08-01  
Lane: SCD mixed-head funnel / protected odd owner-slot bulk / tight
augmenter cover-down  
Status: unconditional probabilistic reservoir theorem with explicit local
degree bounds, exact direct-target census, and exact stratification and
endpoint obstructions.  Exact cover-down of the Delcourt--Postle leave is
not claimed.

## 0. Outcome

Put

\[
 \Omega=[2m-1],\quad
 \mathcal L={\Omega\choose m-1},\quad
 \mathcal M={\Omega\choose m},\quad
 \mathcal U={\Omega\choose m+1},
\]

and

\[
 W=|\mathcal L|=|\mathcal M|,
 \qquad U=|\mathcal U|,
 \qquad C=\operatorname {Cat}_m=W-U.
\]

The mixed-head SCD bank of
`MATH_THEOREM_OWNER_LAYER_SCD_MULTIFUNNEL_RECURRENCE_AND_THREE_PRIMARY_GATE_20260801.md`
has order

\[
 N={2m-3\choose m-2}
   ={m\over2}\operatorname {Cat}_{m-1}.              \tag{0.1}
\]

Unlike four full funnels, this one bank is already resource-disjoint and
born-linear.  The first theorem below shows that it contains a
`C`-element subbank which may be quarantined *with both owner slots at
every endpoint* while the residual odd owner-slot hypergraph remains
asymptotically regular.  Consequently the valid Delcourt--Postle
short-cycle argument builds a physical forest of order `U-o(W)` around
exactly `C` protected, genuinely isolated Johnson providers.

This is a positive Catalan-scale quantifier swap: a protected bank need not
have order `O(sqrt(m))`.  A specially spread bank of order

\[
                    C={2W\over m+1}=\Theta(W/m)       \tag{0.2}
\]

is admissible.

The second half gives the exact limitation.  Fix the two funnel coordinates
`a,z`.  A provider indexed by an SCD pair `S<L` can directly add exactly

\[
 \{aL+b:b\in G-L\}\ \dot\cup\
 \{azS+b:b\in G-L\},\qquad G=\Omega-\{a,z\}.         \tag{0.3}
\]

Thus an upper target `R` has full-bank degree

\[
 d(R)=
 \begin{cases}
  0,&a\notin R,\\
  m,&a\in R,\ z\notin R,\\
  m-2,&a,z\in R.
 \end{cases}                                        \tag{0.4}
\]

The zero row is fatal for an unconditioned leave.  A union of `t`
coordinate-pair banks can reach every upper target only if the set of their
distinguished `a`-coordinates has order at least `m-1`.  In particular no
bounded number of strata can be a universal direct cover-down reservoir.
Four strata leave the explicit macroscopic zero shore

\[
                         {2m-5\choose m+1}.           \tag{0.5}
\]

There is also an exact endpoint cut.  If `a,z in R`, every provider in the
same `(a,z)` stratum which can add `R` consumes the same new owner

\[
                              B=R-z.                 \tag{0.6}
\]

If both slots at `R-z` are unavailable, the target is blocked even when the
entire mixed-head bank is retained.

Therefore the reservoir solves protected bulk planting, but not exact
cover-down.  A successful stratified construction must jointly force the
bulk to cover the zero shore and preserve the named facet tickets (0.6).

## 1. The mixed-head bank as a literal odd-diamond matching

Write

\[
                    \Omega=G\mathbin{\dot\cup}\{a,z\},
                    \qquad |G|=2m-3.
\]

Fix an SCD of `2^G`.  Every rank-`(m-2)` set `S` has a unique successor

\[
                             S<L=\sigma(S),
                    \qquad |L|=m-1.                 \tag{1.1}
\]

The map `sigma` is a bijection from rank `m-2` to rank `m-1`.  The
mixed-head theorem supplies the owner-slot atom

\[
       e_S=(azL,\ aS;\ (aL)^0,\ (azS)^0).            \tag{1.2}
\]

The choice of slot zero in (1.2) is arbitrary.  Its physical Johnson edge
is

\[
                              aL---azS.              \tag{1.3}
\]

The four resource maps

\[
 S\longmapsto aS,\quad azL,\quad aL,\quad azS        \tag{1.4}
\]

are injective, and the two physical endpoint images in (1.4) are
cross-disjoint by their `z`-signature.  Hence

\[
                         \mathcal B=\{e_S:S\in{G\choose m-2}\} \tag{1.5}
\]

is an owner-slot matching whose physical projection is a matching.  Its
order is (0.1).

The exact sampling density needed for a Catalan bank is

\[
 p_m={C\over N}
     ={4(2m-1)\over m(m+1)}
     ={8\over m}+O(m^{-2}).                          \tag{1.6}
\]

In particular `C<=N` for `m>=7`.

## 2. Exact local loss formulas

Let `P` be a subset of `mathcal B`.  Besides the upper and lower resource of every
atom of `P`, quarantine **both** slots of each of its two physical
endpoints.  Thus no later bulk edge can meet a physical endpoint of `P`,
and every edge of `P` remains an isolated component.

Let

\[
 \mathcal R_P\subseteq\mathcal U,\qquad
 \mathcal L_P\subseteq\mathcal L,\qquad
 \mathcal V_P\subseteq\mathcal M                  \tag{2.1}
\]

be respectively its upper colours, lower colours and physical endpoints.
All have orders `|P|,|P|,2|P|`.

The complete odd owner-slot host has degrees

\[
 d(R)=2m(m+1),\qquad d(L)=d(T^i)=2m(m-1),           \tag{2.2}
\]

and maximum codegree at most `2m`.

### Lemma 2.1 (upper-star formula)

For an unquarantined `R` in `mathcal U`, put

\[
 A_R=|\{L\in\mathcal L_P:L\subset R\}|,
 \qquad
 Q_R=|\{T\in\mathcal V_P:T\subset R\}|.            \tag{2.3}
\]

Then the surviving degree is exactly four times the number of pairs
`{x,y} subset R` for which

\[
 R-\{x,y\}\notin\mathcal L_P,qquad
 R-x,R-y\notin\mathcal V_P.                         \tag{2.4}
\]

Consequently

\[
 d(R)-d_P(R)
 \le 4A_R+4\left(mQ_R-{Q_R\choose2}\right)
 \le 4A_R+4mQ_R.                                    \tag{2.5}
\]

Moreover the candidate classes before sampling satisfy

\[
 A_R^{\rm all}\le {m+1\choose2},
 \qquad Q_R^{\rm all}\le m+1.                      \tag{2.6}
\]

#### Proof

An atom through `R` is determined physically by a pair `{x,y} subset R`,
with lower resource `R-{x,y}` and owner facets `R-x,R-y`.  If all three
physical resources survive, there are four choices of their two slot
labels; otherwise there are none because both slots at a quarantined owner
were deleted.  This proves (2.4).

There are `A_R` bad lower pairs.  If `Q_R` facets are bad, the number of
pairs containing at least one of their deleted-element labels is

\[
 {m+1\choose2}-{m+1-Q_R\choose2}
 =mQ_R-{Q_R\choose2}.
\]

The union bound gives (2.5).  Finally `R` has
`binom(m+1,2)` lower two-facets and `m+1` owner facets, proving (2.6).
\(\square\)

### Lemma 2.2 (lower-star formula)

For an unquarantined `L` in `mathcal L`, put

\[
 A_L=|\{R\in\mathcal R_P:L\subset R\}|,
 \qquad
 Q_L=|\{T\in\mathcal V_P:L\subset T\}|.             \tag{2.7}
\]

Then

\[
 d(L)-d_P(L)
 \le4A_L+4\left((m-1)Q_L-{Q_L\choose2}\right)
 \le4A_L+4(m-1)Q_L,                                 \tag{2.8}
\]

and

\[
 A_L^{\rm all}\le {m\choose2},
 \qquad Q_L^{\rm all}\le m.                        \tag{2.9}
\]

#### Proof

Use the pair of added elements in `Omega-L`.  There are `m` possible owner
supersets; a bad one lies in `Q_L(m-1)-binom(Q_L,2)` pairs.  The rest is
identical to Lemma 2.1. \(\square\)

### Lemma 2.3 (owner-slot formula)

Let `T^i` survive.  Put

\[
\begin{aligned}
 Q_T^-&=|\{L\in\mathcal L_P:L\subset T\}|,\\
 Q_T^+&=|\{R\in\mathcal R_P:T\subset R\}|,\\
 J_T&=|\{H\in\mathcal V_P:|T-H|=|H-T|=1\}|.
\end{aligned}                                        \tag{2.10}
\]

Then

\[
 d(T^i)-d_P(T^i)
 \le2\big((m-1)Q_T^-+mQ_T^++J_T\big),              \tag{2.11}
\]

and

\[
 (Q_T^-)^{\rm all}\le m,\qquad
 (Q_T^+)^{\rm all}\le m-1,\qquad
 J_T^{\rm all}\le m(m-1).                          \tag{2.12}
\]

#### Proof

The star of `T^i` is indexed by `(x,y) in T times (Omega-T)`.  Its lower,
upper and other physical owner are

\[
                     T-x,\qquad T+y,\qquad T-x+y.   \tag{2.13}
\]

There are two choices for the other owner slot if all three resources
survive and zero if its physical owner is quarantined.  A bad lower fixes
`x` and removes `m-1` pairs; a bad upper fixes `y` and removes `m` pairs;
a bad neighbouring owner removes one pair.  Multiplication by the two
other-slot choices and a union bound prove (2.11).  The candidate counts
in (2.12) are the numbers of facets, cofacets and Johnson neighbours of
`T`. \(\square\)

These formulas are the exact replacement for the unusable crude estimate
`|P| Delta_2`.

## 3. A simultaneous hypergeometric bound

### Theorem 3.1 (Catalan isolated reservoir)

For all sufficiently large `m`, there is a subbank

\[
                         P\subseteq\mathcal B,
                         \qquad |P|=C,               \tag{3.1}
\]

such that, after the quarantine in Section 2, every surviving host vertex
has degree

\[
             d_P(v)=d(v)-O\left({m^2\over\log m}\right)
                   =(1-o(1))d(v).                   \tag{3.2}
\]

The conclusion remains true in the presence of any prescribed
resource-disjoint physical forest `P_0` of order `O(sqrt(m))`, after
discarding the `O(sqrt(m))` bank atoms meeting its resources or physical
owners and quarantining `P_0` as well.

#### Proof

First take `P_0` empty.  Choose `P` uniformly among the `C`-subsets of
`mathcal B`.  By (1.6), the inclusion density is at most `9/m` for all
sufficiently large `m`.

If `X` counts the selected members of any fixed `K`-element candidate
class, then `X` is hypergeometric, has mean at most `9K/m`, and obeys

\[
          Pr(X\ge t)\le\left({e\,E X\over t}\right)^t
                                                        \tag{3.3}
\]

whenever `t>=E X`.

Put

\[
                t_1={24m\over\log m},
                \qquad t_2={24m^2\over\log m}.       \tag{3.4}
\]

For a candidate class of order at most `m+1`, (3.3) gives

\[
             Pr(X>t_1)\le \exp(-(12-o(1))m).         \tag{3.5}
\]

Here and below an owner count is allowed to contain both endpoints of one
bank atom.  Replace it by the number of underlying bank atoms: the owner
count is at most twice that hypergeometric variable.  This is the factor
two already absorbed in the exponent `12` in (3.5).  Upper and lower
resource counts have multiplicity one.

For a class of order at most `binom(m+1,2)` or `m(m-1)`, it gives

\[
             Pr(X>t_2)\le \exp(-\Omega(m^2)).        \tag{3.6}
\]

There are fewer than

\[
                         4W<2^{2m+1}                 \tag{3.7}
\]

host vertices.  Since `12>2 log 2`, a union bound over every class in
(2.6), (2.9) and (2.12) shows that with positive probability all
facet/cofacet counts are at most `t_1` and all two-shadow/Johnson counts
are at most `t_2` simultaneously.

On that event Lemmas 2.1--2.3 give, respectively,

\[
\begin{aligned}
 d(R)-d_P(R)&\le4t_2+4mt_1,\\
 d(L)-d_P(L)&\le4t_2+4(m-1)t_1,\\
 d(T^i)-d_P(T^i)&\le2((2m-1)t_1+t_2),
\end{aligned}                                        \tag{3.8}
\]

which is (3.2).

Now include `P_0`.  Because each of the four resource maps in (1.4) is
injective, at most `O(|P_0|)=O(sqrt(m))` bank atoms meet a resource or
physical owner of `P_0`.  Delete them before sampling.  The sampling density
is still at most `9/m`.  Quarantining all resources and both owner slots of
`P_0` lowers a surviving degree by at most

\[
              O(|P_0|\Delta_2)=O(m^{3/2})=o(m^2),   \tag{3.9}
\]

so the same proof applies. \(\square\)

### Corollary 3.2 (protected high-girth bulk around `C` isolated providers)

For all sufficiently large `m`, the odd owner-slot host has a matching
`F` such that

1. `P subseteq F` for a bank `P` as in Theorem 3.1;
2. all `C` physical edges of `P` are isolated components of the physical
   projection of `F`;
3. the physical projection of `F` is a linear forest; and
4.

\[
                              |F|=U-o(W).             \tag{3.10}
\]

Any fixed protected pivot forest of order `O(sqrt(m))` may be retained as
well.

#### Proof

Delete the quarantined vertices and work in the residual host.  Theorem
3.1, the original maximum-codegree bound `2m=o(m^2)`, and the fact that
`C=o(W)` give an asymptotically regular residual four-graph with

\[
                      (U-C-o(W))(1-o(1))2m(m+1)     \tag{3.11}
\]

edge incidences on its upper shore.

For any fixed cycle cutoff `g`, apply the audited Delcourt--Postle
conflict-free colouring with projected cycles of lengths `3,...,g`
forbidden.  A largest colour class has order `U-C-o_g(W)` and no physical
cycle of length at most `g`.  It is physically disjoint from `P` because
both slots of every endpoint in `P` were quarantined.

Adjoin `P`, delete one residual edge from every remaining long cycle, and
take the standard slow diagonal `g=g(m)->infinity`.  At most `o(W)` edges
are lost.  No edge of `P` is deleted and every such edge stays isolated.
This proves (3.10). \(\square\)

### Proposition 3.3 (exact residual-slot ledger)

Keep `C` isolated providers and their complementary endpoint slots
quarantined.  If the residual bulk has order

\[
                              U-C-s,                 \tag{3.12}
\]

then it leaves exactly `2s` exterior owner slots unused.  Activating `s`
of the providers by tight one-to-two augmenters reaches total order `U`
and consumes exactly those `2s` exterior slots.  The `2C` complementary
slots at the provider endpoints remain the final degree-one endpoint bank.

#### Proof

The `2C` provider endpoints account for `4C` quarantined slot vertices, so
the residual host has

\[
                            2W-4C                 \tag{3.13}
\]

exterior slots.  A matching of order `U-C-s=W-2C-s` uses

\[
                            2W-4C-2s              \tag{3.14}
\]

of them.  This leaves `2s`.  The starting family has order

\[
                    C+(U-C-s)=U-s.                 \tag{3.15}
\]

Every tight activation retains the two used provider slots and adds one
`B` slot and one `D` slot, increasing the order by one.  After `s`
activations the order is `U`, all exterior slots are used, and precisely
the unused complementary slot at each of the `2C` provider endpoints
remains. \(\square\)

In particular exact residual upper saturation (`s=0`) is the wrong target:
it consumes every exterior slot and leaves no direct-augmenter ticket.  The
correct bulk theorem must deliberately export its target leave and its
`2s` endpoint slots together.

### Scope

The error `o(W)` in (3.10) is not known to be at most `C`, and the leave is
not prescribed.  Thus (3.10) by itself does not provide enough installed
augmenters to close every omitted upper colour.

## 4. Exact anonymous target-neighbour census

This section works in the physical owner-slot model before a predecessor
matching `M_0` and rooted phase are imposed.  Rooting can only delete the
target incidences counted here, so every zero or endpoint cut below remains
necessary in the rooted model.

Fix `S<L=S+x` in the SCD bank.  Its provider atom has

\[
  L_0=aS,qquad A=aL=L_0+x,qquad C_0=azS=L_0+z,
  \qquad A\cup C_0=azL.                             \tag{4.1}
\]

In the tight one-to-two augmenter, retain first `A` and then `C_0`.  If
`b in G-L`, the two possible target colours are

\[
                   aL+b,\qquad azS+b.               \tag{4.2}
\]

Conversely every target obtainable directly from this provider has one of
the two forms (4.2).  Hence the provider degree is exactly `2(m-2)`.

### Theorem 4.1 (exact anonymous full-bank target degrees)

In the bipartite graph from upper targets to all providers in `mathcal B`,
the target degree is (0.4).

#### Proof

If `a notin R`, (4.1) shows that no target diamond can use a provider from
the bank.

Suppose `R=aU` with `U in binom(G,m)`.  Every rank-`(m-1)` facet `L` of
`U` has a unique SCD predecessor `S`, and with `b=U-L` the first form in
(4.2) gives `R`.  These are the `m` neighbours, and there are no others.

Suppose `R=azV` with `V in binom(G,m-1)`.  The second form in (4.2)
requires `V=S+b`, where `S` is a facet of `V`, and also
`b notin L=sigma(S)`.  There are `m-1` facets `S`.  Exactly one of them is
the predecessor `sigma^{-1}(V)`; for it `b` is the SCD-added element and is
forbidden.  Every other facet is legal.  Thus the degree is `m-2`.
\(\square\)

The zero-degree shore has exact order

\[
                    |\{R\in\mathcal U:a\notin R\}|
                    ={2m-2\choose m+1}.             \tag{4.3}
\]

It is a positive fraction of the entire upper layer.

## 5. No bounded stratification can remove the zero shore

Consider `t` mixed-head banks, not necessarily using the same SCD or the
same `z`-coordinate.  Let

\[
                       A=\{a_1,\ldots,a_t\}          \tag{5.1}
\]

be their distinct compulsory target coordinates.

### Theorem 5.1 (sharp support threshold)

If the union of the `t` direct-target graphs reaches every member of
`mathcal U`, then

\[
                              |A|\ge m-1.             \tag{5.2}
\]

In particular `t>=m-1`; no bounded number of coordinate-pair strata can
be a universal direct cover-down reservoir.

The bound is sharp as a statement about coordinate support: every
`(m+1)`-set meets every fixed `(m-1)`-set `A`.

#### Proof

Every target reached from bank `i` contains `a_i`, by Theorem 4.1.  If
`|A|<=m-2`, then

\[
                         |\Omega-A|\ge m+1,
\]

so an `(m+1)`-subset of `Omega-A` is an upper target with no neighbour.
Conversely, if `|A|=m-1`, the complement has order `m`, so no upper target
can avoid all of `A`.  This proves the support claim only; it does not
assert provider or endpoint Hall. \(\square\)

For four distinct compulsory coordinates the zero shore has order (0.5).
Indeed it consists of the `(m+1)`-subsets of a `(2m-5)`-element complement.
Its relative density is

\[
 { {2m-5\choose m+1}\over {2m-1\choose m+1}}
 ={(m-2)(m-3)(m-4)(m-5)\over
   (2m-1)(2m-2)(2m-3)(2m-4)}
 \longrightarrow {1\over16}.                       \tag{5.3}
\]

Thus four strata do not merely miss a few exceptional targets; they miss a
macroscopic shore.

## 6. The common facet-ticket cut

The target census has a second, occurrence-level consequence.

### Theorem 6.1 (forced `B` endpoint)

Let `R=azV`.  For every provider `S<L` adjacent to `R`, the target diamond
in the tight augmenter uses the same new physical owner

\[
                             B=R-z=aV.               \tag{6.1}
\]

The other new owner has the form

\[
                             D_y=azL-y,
                             \qquad y\in aS,          \tag{6.2}
\]

and the corresponding new lower resource is

\[
                             L'_y=(aS-y)+x,           \tag{6.3}
\]

where `x=L-S`.  Thus all provider freedom leaves the singleton facet bank
`{R-z}` unchanged.

#### Proof

For the second orientation in (4.2), write `R=azS+b`.  The new target
owner which does not belong to the old provider is

\[
                         B=L_0+b=aS+b=aV=R-z.
\]

In the general augmenter formula, choosing the deleted element `y in L_0`
gives

\[
 D_y=(L_0-y)+z+x=azL-y,
 \qquad L'_y=(L_0-y)+x,
\]

which proves (6.2)--(6.3). \(\square\)

### Corollary 6.2 (endpoint singleton cut)

If both owner slots at `R-z` are occupied or forbidden in the background
forest, no direct tight augmenter from the `(a,z)` mixed-head bank can add
`R`, even if all `N` providers are available.

For several strata, a target `R` for which every usable distinguished
coordinate `a_i in R` also has `z_i in R` has candidate new-owner bank

\[
                         \{R-z_i:a_i,z_i\in R\}.      \tag{6.4}
\]

The free endpoint slots on (6.4) therefore obey an ordinary Hall cut before
the lower and `D_y` resources are considered.

The isolation in Corollary 3.2 makes the graphic part of one augmentation
easy: after deleting its provider edge, the two retained endpoints are
isolated, so attaching them to free `B,D_y` endpoints cannot create a
cycle.  It does not make the endpoint tickets in (6.1)--(6.3) free.

### Proposition 6.3 (exact private-exterior packet reduction)

Let `Z` be a target leave and `P` an isolated provider bank.  Form the
five-partite packet hypergraph with parts

\[
 Z,\qquad P,\qquad \mathcal L_{\rm free},\qquad
 (\mathcal M\times\{0,1\})_{B,\rm free},\qquad
 (\mathcal M\times\{0,1\})_{D,\rm free}.            \tag{6.5}
\]

For every target/provider orientation and every `y` in the provider lower
set, put in the packet edge

\[
                         (R,e_S,L'_y,B^p,D_y^q)      \tag{6.6}
\]

when the two slots are free and the identities of the tight augmenter
hold.  Restrict to the **private exterior face** on which the physical
owners `B,D_y` lie outside all reservoir endpoints and distinct packet
edges use distinct physical exterior owners.

On this face, a simultaneous family of direct tight augmenters saturating
`Z` exists if and only if (6.5) has a matching saturating `Z`.

#### Proof

The tight augmenter retains the old upper, lower and two provider-slot
resources and adds exactly `R,L'_y,B^p,D_y^q`.  Thus owner-slot
resource-disjointness is exactly hypergraph matching in (6.5).  After the
old provider edge is removed, each of its two physical endpoints is
isolated.  On the private exterior face the two new physical edges attach
these isolated vertices as leaves to two exterior forest vertices.  Across
packets all four leaf/exterior roles are disjoint, so no physical cycle or
degree-three vertex is created.  Conversely every direct packet exposes
one edge (6.6). \(\square\)

Without the private-exterior restriction, (6.5) remains a necessary
resource condition but a separate graphic cut is required.  Even on the
private face, ordinary target/provider Hall is not sufficient: the `B`,
`D` and lower parts must be matched simultaneously.  Corollary 6.2 is the
smallest possible failed cut in the `B` part.

## 7. Revised exact frontier

The unconditional chain is now

\[
 \boxed{
 \begin{array}{c}
 \text{one resource-disjoint mixed-head SCD bank}\\
 \Downarrow\\
 C\text{ uniformly spread isolated providers}\\
 \Downarrow\\
 \text{protected odd physical forest of size }U-o(W).
 \end{array}}
                                                               \tag{7.1}
\]

What does **not** follow is

\[
 \text{arbitrary }o(W)\text{ upper leave}
 \longrightarrow
 \text{tight-augmenter cover-down}.                              \tag{7.2}
\]

The exact reasons are:

1. the Delcourt--Postle error is not proved to be at most `C`;
2. one stratum has the zero shore (4.3);
3. every bounded collection has the zero shore of Theorem 5.1; and
4. even on the positive shore, (6.1) is a forced endpoint ticket.

A viable stratified remedy must therefore use at least `m-1` compulsory
coordinates, or force the bulk to saturate every target outside a smaller
chosen target shore.  It must then select a resource-disjoint provider
subbank and a background forest **jointly**, with free facet slots satisfying
the cuts (6.4), plus the `D_y` and lower-resource cuts in (6.2)--(6.3).

The local regularity calculation is no longer the obstacle: any such
`O(C)` isolated bank with the same `O(m/log m)` facet and
`O(m^2/log m)` two-shadow loads can be protected by the proof of Theorem
3.1.  The remaining theorem is a stratified target/endpoint selector, not
another Delcourt--Postle invocation.

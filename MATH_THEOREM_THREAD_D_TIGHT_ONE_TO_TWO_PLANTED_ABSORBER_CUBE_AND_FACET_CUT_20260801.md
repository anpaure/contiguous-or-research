# Tight one-to-two absorbers: a planted cube and the exact facet cut

Date: 2026-08-01  
Lane: Thread D / prospective `M0` / off-support torsion absorption  
Status: unconditional local obstruction and unconditional planted-bank
theorem; completion around the planted bank remains a separate hypothesis.

## 0. Outcome

The tight one-to-two augmenter has an exact directed form compatible with
the prospective-`M0` system.  It is not merely a clone-capacity move.  In
one phase it consists of an auxiliary diamond and one residual incidence
edge; in the other phase it consists of the target diamond and a rerouted
copy of the auxiliary colour.  It therefore consumes exactly one residual
`L -> T` slot and one unused head.

This yields a positive bounded-defect theorem.  Any sufficiently small set
of target colours can be assigned pairwise resource-disjoint augmenters,
away from a protected tight-pivot bank.  If the remaining Boolean system is
completed while respecting the prescribed auxiliary diamonds and residual
slots, the selected gadgets form a literal `2^k` absorber cube: every
subset of the targets can be switched independently, all prospective rows
remain exact, and both phases are directed linear forests.  Consequently
every cut in the planted absorber rank is tight with value equal to its
number of target colours.

The raw polynomial census and the `C=Cat_m` scalar slack do **not** imply
this expansion for an arbitrary partial state.  Every direct service of a
target `R` consumes a free owner clone on the middle-facet boundary of `R`.
For every `m>=4` there is a literal directed-linear-forest matching which
occupies both roles of every such facet, so the target has no direct tight
augmenter.  Total Catalan slack can also be placed entirely off that
boundary.  Alternating rerouting or prospective planting is therefore
essential.

The theorem is useful only after a recursive/off-support rounding has
compressed its exported defect to `o(m)` (in particular `O(1)`).  It does
not independently absorb the linear bank of local defects obtained by
rounding every `Q_3` support block in place.

## 1. Directed form of the frozen augmenter

Let `Omega` have size `2m-1`.  Use lower sets of size `m-1`, owners of size
`m`, and upper colours of size `m+1`.  Fix an upper colour `R`.  Choose
ordered distinct `a,b in R`, put

\[
 L=R-\{a,b\},
\]

choose `c notin R` and `x in L`, and define

\[
\begin{array}{lll}
 A=L+a,&B=L+b,&C=L+c,\\
 L'=(L-x)+c,&D=(L-x)+a+c,&S=L+a+c.
\end{array}                                                   \tag{1.1}
\]

Orient the three diamonds as

\[
 f=(S;L,A,C),\qquad e=(R;L,A,B),\qquad
 g=(S;L',D,C),                                                \tag{1.2}
\]

and put

\[
                         y=(L',D).                            \tag{1.3}
\]

Here a displayed diamond `(Q;K,T,V)` is the rooted arc `T -> V`.

### Lemma 1.1 (exact prospective lift)

In the prospective oriented-diamond system the two local states

\[
                 (X^-,Y^-)=(\{f\},\{y\}),\qquad
                 (X^+,Y^+)=(\{e,g\},\varnothing)             \tag{1.4}
\]

have identical loads on every old lower, tail, head, and auxiliary-colour
resource.  The plus state additionally covers `R`; relative to the minus
state it consumes exactly the residual edge `L' -> D` and the previously
unused head `B`.

Both rooted supports are directed linear forests.  The minus support is
the edge `A -> C`; the plus support is the two-edge matching
`A -> B, D -> C`.

#### Proof

The identities

\[
 A\cap C=L,\ A\cup C=S,\quad
 A\cap B=L,\ A\cup B=R,
\]

and

\[
 D\cap C=L',\qquad D\cup C=S,
\]

prove legality.  The lower/tail pairs used in the minus phase are
`(L,A)` and `(L',D)`; those used in the plus phase are the same two pairs,
now both carried by diamonds.  The old head `C` and colour `S` occur once
in both phases.  The only new head and colour are `B` and `R`.  Finally
`A,B,C,D` are pairwise distinct, so the two displayed plus edges are
disjoint.  This proves every assertion.  \(\square\)

The aligned strict directed subfamily (1.1)--(1.3) has exactly

\[
             N_m=(m+1)m(m-2)(m-1)                              \tag{1.5}
\]

members through a fixed `R`.  Reversing every rooted arc gives the second
strict typed lift.  The factor sixteen in the frozen owner-slot theorem
instead labels anonymous physical-owner copies and must not be identified
with tail/head roles.

## 2. The exact facet cut

Write

\[
        \partial R=\{B\in {\Omega\choose m}:B\subset R\}.
\]

In (1.1), `B` is always a member of `partial R`.  Thus every directed
augmenter of the phase (1.2) consumes one unused head in `partial R`.
The reversed phase consumes one unused tail in `partial R`.

### Proposition 2.1 (necessary boundary Hall cut)

For any family `D` of missing colours, every simultaneous family of direct
tight augmenters satisfies

\[
 |D'|\le
 \left|H_0\cap\bigcup_{R\in D'}\partial R\right|               \tag{2.1}
\]

for each subfamily `D'` if all target arcs use orientation (1.2), where
`H_0` is the unused-head bank.  In the two-clone unoriented host the right
side is replaced by the number of free clones on the same facet union.

#### Proof

The target diamond of an augmenter for `R` uses its new owner `B` on the
middle-facet boundary of `R`.  Distinct simultaneous augmenters must use
distinct head resources (or distinct owner clones).  Injection gives
(2.1).  \(\square\)

The scalar slack does not force (2.1).  Indeed

\[
 W-(m+1)\ge C+1                                              \tag{2.2}
\]

for every `m>=3`, because `W-C=|U|>=m+2`.  Hence the `C+1` unused heads of
a one-defect partial state can, at the level of resource counts, all lie
outside `partial R`.

There is also a literal local matching obstruction, not just a capacity
profile.

### Proposition 2.2 (a forest-saturated facet blocker)

For every `m>=4` and every upper `R`, there is an owner-role matching of
`2(m+1)` genuine diamonds whose rooted support is a disjoint union of
directed two-edge paths and which occupies both the tail and head role of
every owner in `partial R`.  Consequently `R` has no direct tight
one-to-two augmenter in either orientation.

#### Proof

Write `R={a_i:i in Z_(m+1)}` and choose distinct `c_0,c_1` outside `R`.
Put

\[
\begin{aligned}
 T_i&=R-a_i,\\
 L_{i,s}&=R-\{a_i,a_{i+s+1}\},\\
 V_{i,s}&=L_{i,s}+c_s,\\
 S_{i,s}&=T_i+c_s,
 \qquad s\in\{0,1\}.
\end{aligned}                                                \tag{2.3}
\]

Take the arc `T_i -> V_(i,0)` for `s=0` and the arc
`V_(i,1) -> T_i` for `s=1`.  The upper colours are distinct because they
record `(i,c_s)`.  The lowers are distinct because, on a cycle of length
at least five, the unordered pairs `{i,i+1}` and `{i,i+2}` occur only once
in this list.  All `V_(i,s)` are distinct and lie outside the facet bank.
Thus the support is the disjoint union

\[
                       V_{i,1}\to T_i\to V_{i,0}.             \tag{2.4}
\]

Every facet `T_i` is used once as a tail and once as a head.  A target
diamond of colour `R` necessarily uses two facets of `R`; whichever way it
is oriented, its new facet role is occupied.  \(\square\)

Proposition 2.2 is a local obstruction.  It is not asserted that this
particular bank extends to a full prospective state.  It is enough to rule
out any all-cut theorem deduced solely from local augmenter degree, scalar
Catalan slack, and linear-forest topology.

## 3. A quantitative planted-bank theorem

For a fixed target `R`, call an upper token, lower token, or physical-owner
token forbidden if a prospective augmenter is required to avoid it.  Let
`d_R(z)` be the number of structural configurations (1.1) containing the
token `z` among

\[
                      R,S,L,L',A,B,C,D.                         \tag{3.1}
\]

The target token `R` itself is excluded from this definition.

### Lemma 3.1 (token codegree)

For every non-target token,

\[
 d_R(z)\le
 \Delta_m:=2m(m-2)(m-1).                                      \tag{3.2}
\]

Consequently any forbidden token set `Z` with

\[
 |Z|<\eta_m:=\frac{N_m}{\Delta_m}
 =\frac{m+1}{2}                                                \tag{3.3}
\]

misses at least one augmenter through `R`.

#### Proof

For completeness, the largest multiplicities before forgetting owner
roles are

\[
\begin{array}{c|c}
\text{token position}&\text{maximum multiplicity}\\ \hline
S&m(m-1)\\
L&2(m-2)(m-1)\\
L'&6\\
A&m(m-2)(m-1)\\
B&m(m-2)(m-1)\\
C&2(m-1)\\
D&2(m-1).
\end{array}                                                   \tag{3.4}
\]

A fixed physical owner contained in `R` can occur in the `A,B` positions,
for total multiplicity at most `2m(m-2)(m-1)`.  A physical owner not
contained in `R` can occur only in the `C,D` positions, for total
multiplicity at most `4(m-1)`.  These cases are disjoint, and the former is
larger for `m>=3`.  Upper and lower multiplicities are smaller.
The union bound deletes at most `|Z| Delta_m` of the `N_m` configurations,
which proves (3.3).  \(\square\)

The weighted version is often stronger: an augmenter survives whenever

\[
                         \sum_{z\in Z}d_R(z)<N_m.              \tag{3.5}
\]

This is the appropriate test after quarantining a large quotient bank;
its cardinality alone need not reflect its local conflict with `R`.

### Theorem 3.2 (resource-disjoint planted augmenter bank)

Let `D` be a set of `k` distinct target colours.  Let `P` be a protected
set of `p` upper, lower, and physical-owner tokens, with no target colour
in `P`.  If

\[
                    p+8(k-1)<\eta_m,                            \tag{3.6}
\]

then the targets admit augmenters (1.1), one per target, such that

1. all eight token sets (3.1) are pairwise disjoint;
2. no token meets `P`;
3. no auxiliary colour `S_i` belongs to `D`; and
4. the minus and plus rooted supports are both linear forests and are
   vertex-disjoint from the protected rooted support.

#### Proof

Choose the targets greedily.  When processing `R_i`, forbid `P`, the other
`k-1` target colours, and all tokens of previously chosen gadgets.  A prior
gadget contributes eight tokens, but its target colour is already among
the other target colours, so the number of forbidden tokens is at most

\[
                       p+(k-1)+7(i-1)\le p+8(k-1).
\]

Lemma 3.1 gives an available configuration.  Token disjointness gives all
partition-resource assertions.  Physical-owner disjointness makes the
minus edges `A_i C_i` a matching and the plus edges
`A_i B_i,D_i C_i` a matching, each disjoint from the protected support.
Thus both supports are forests.  \(\square\)

In particular, for a tight pivot using `p=O(h)` tokens with `h=o(m)`, every
fixed `k=O(1)` target bank satisfies (3.6) for all sufficiently large `m`.

## 4. The absorber cube and exact all-cut expansion

The preceding theorem plants local data.  The following statement cleanly
separates it from the still-open completion of the free bulk.

### Theorem 4.1 (conditional regenerative absorber cube)

Let the gadgets from Theorem 3.2 be indexed by `D`.  Suppose there is a
prospective background state `(X_0,Y_0)` such that

* `X_0` covers every upper colour outside `D union {S_i:i in D}`;
* it is resource-disjoint from every gadget token;
* `(X_0,Y_0)` together with all `f_i` and all residual pairs
  `y_i=(L_i',D_i)` satisfies every lower/tail equality; and
* the rooted support of `X_0`, including the protected tight pivot, is a
  linear forest disjoint from the gadget owners.

For every subset `J subset D`, define

\[
\begin{aligned}
X_J={}&X_0
 \cup\{e_i,g_i:i\in J\}
 \cup\{f_i:i\in D-J\},\\
Y_J={}&Y_0\cup\{y_i:i\in D-J\}.                         \tag{4.1}
\end{aligned}
\]

Then `(X_J,Y_J)` is an exact prospective state, its selected arcs form a
linear forest, and its covered target set is exactly `J`.  In particular
`J=D` is a full upper-colour state preserving the tight pivot.

Moreover, for every `A subset D`, the maximum simultaneous-packet rank on
the planted candidates satisfies

\[
                              \nu^{1\to2}(A)=|A|.               \tag{4.2}
\]

Thus every absorber cut has equality: the planted bank has literal all-cut
expansion.

#### Proof

Apply Lemma 1.1 independently on the pairwise resource-disjoint gadgets.
It proves every partition equality and preserves each auxiliary colour.
The gadgets and the background are vertex-disjoint forests, so their union
is a forest in every phase.  The candidates indexed by any `A` are
simultaneously applicable, proving a packet of size `|A|`;
the colour partition gives the reverse inequality in (4.2).  \(\square\)

The resource ledger is exact.  Before all `k` switches there are `U-k`
diamonds and `C+k` residual incidence edges; afterwards there are `U`
diamonds and `C` residual edges.  The transition consumes exactly the `k`
planted residual pairs and `k` planted heads.  It asks for no slack beyond
the intrinsic Catalan surplus.

## 5. Consequences for higher torsion and the quotient bank

Theorem 4.1 identifies the useful scope of the new primitive.

* It **does** close any `O(1)` exported colour defect once a recursive
  off-support rounding supplies the background completion in Theorem 4.1.
  The pivot can be frozen literally.
* It **does not** round the disjoint `Q_3` support bank one block at a time.
  That bank has `Omega(U)` local support defect, whereas the crude planted
  margin (3.6) handles only `o(m)` targets.  A recursive bulk reroute must
  first compress the live boundary.
* The `Cat_r` isolated quotient sectors may be quarantined before planting.
  For that large bank one must verify the weighted local inequality (3.5),
  not substitute its cardinality for `p`.  No such uniform weighted bound
  is proved here.
* For an arbitrary already-rounded partial state, Proposition 2.1 is an
  unavoidable first separator.  If it fails, monotone one-to-two moves
  cannot start; a colour transposition or a longer alternating tree must
  first release a facet resource.

Accordingly the precise surviving theorem is: **bounded exported torsion is
absorbable by a preplanted tight augmenter cube, conditional only on a
bulk prospective/graphic completion avoiding its constant token bank.**
The remaining all-dimensional gate is that completion (or an alternating
expansion theorem strong enough to manufacture the same cube dynamically),
not the local absorber algebra.

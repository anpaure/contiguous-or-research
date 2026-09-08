# Heptagonal cap circulations: an exact `C14` absorber template and its prospective abundance

**Date:** 2026-08-02  
**Status:** unconditional local algebra and central-token counting; conditional
physical-history spread.  This note separates the finite `k=17` witness from
the still-open uniform host/regeneration theorem.

## 1. A uniform seven-row circuit

Fix `k,r` with `r>=3` and `k-r>=5`.  Fix a rank-`r` owner `X` and a
distinguished coordinate `a in X`.  Choose ordered coordinates

\[
 b,c\in X\setminus\{a\},\qquad
 p,q,s,t\in[k]\setminus X,                               \tag{1.1}
\]

all distinct, and put

\[
 C=X\setminus\{a,b,c\}.                                  \tag{1.2}
\]

Choose one more coordinate

\[
 z\notin C\cup\{a,b,c,p,q,s,t\}.                         \tag{1.3}
\]

On the seven active labels define

\[
\begin{array}{c|c}
i&H_i\\ \hline
0&abc\\
1&abp\\
2&apq\\
3&pqs\\
4&cps\\
5&cpt\\
6&bct.
\end{array}                                                \tag{1.4}
\]

Consecutive triples differ by one exchange, including `H_6,H_0`.  Put

\[
 x_i=C\cup H_i,qquad
 f_i=C\cup(H_i\cap H_{i+1}),qquad
 y_i=f_i\cup\{z\}.                                       \tag{1.5}
\]

All indices are modulo seven.

### Theorem 1 (cap-exact heptagonal circulation)

The seven old rows

\[
 e_i=\{x_i,y_i\}\quad\hbox{at facet }f_i               \tag{1.6}
\]

may be replaced by

\[
 e_i'=\{x_{i+1},y_i\}.                                   \tag{1.7}
\]

The replacement has all of the following exact properties.

1. It is a simple endpoint-retaining alternating `C14` in the
   owner--facet incidence graph.
2. Every facet row and every owner degree is unchanged.
3. The immediate-upper cap multiset is unchanged, not merely its support.

#### Proof

Every `H_i cap H_{i+1}` has size two, so `f_i` has rank `r-1`; both moving
owners and `y_i` contain it and have rank `r`.  The seven intersections in
(1.4) are

\[
 ab,ap,pq,ps,cp,ct,bc,                                    \tag{1.8}
\]

and are distinct.  The moving owners are distinct, and every retained owner
contains `z` while no moving owner does, so no unintended owner equality or
edge equality occurs.  Deleting `x_i-f_i` and inserting `x_{i+1}-f_i`
gives the alternating circuit

\[
 x_0-f_0-x_1-f_1-\cdots-x_6-f_6-x_0.                    \tag{1.9}
\]

Thus moving-owner degrees telescope and retained incidences stay fixed.

Finally, the old and new caps in row `i` are

\[
 U_i=C\cup H_i\cup\{z\},\qquad
 U_i'=C\cup H_{i+1}\cup\{z\}=U_{i+1}.                  \tag{1.10}
\]

Hence the new cap list is a cyclic permutation of the old list. \(\square\)

This is stronger than the authenticated `k=17` circuit, which sometimes
uses duplicated-cap slack or a mixture of cap transport and slack.  The
fixed `z` template is a uniform cap-multiset-exact subclass.

## 1.1 Equivariant holonomy and the exact cap-transport condition

Let `rho` generate a free `Z_m` action.  A quotient endpoint circuit of row
length `t` has representatives `x_i,y_i,f_i` and phase increments `a_i`
such that its phase-`g` rows are

\[
 \{\rho^g x_i,\rho^g y_i\}
 \longmapsto
 \{\rho^{g+a_i}x_{i+1},\rho^g y_i\}.                    \tag{1.11}
\]

The row geometry requires

\[
 f_i=x_i\cap y_i=\rho^{a_i}x_{i+1}\cap y_i.              \tag{1.12}
\]

Put

\[
 h=\sum_i a_i\pmod m,qquad
 U_i=x_i\cup y_i,qquad
 V_i=\rho^{a_i}x_{i+1}\cup y_i.                          \tag{1.13}
\]

### Theorem 1.1 (voltage and cap circulation)

Assume the involved owner, facet, and cap orbits are free.

1. The developed moving graph has `gcd(m,h)` circuits, each of row length
   `tm/gcd(m,h)`.
2. If `mu^-(O)` and `mu^+(O)` count the `U_i` and `V_i` in cap orbit `O`,
   then the quotient cap-load identity is

   \[
       M'(O)=M(O)-\mu^-(O)+\mu^+(O).                    \tag{1.14}
   \]

   Immediate-upper support is preserved iff the right side is at least one
   for every cap orbit.
3. The cap multiset is preserved exactly iff there are a permutation `pi`
   of the rows and shifts `q_i in Z_m` such that

   \[
                         V_i=\rho^{q_i}U_{\pi(i)}.        \tag{1.15}
   \]

#### Proof

Following one quotient lap adds phase `h`; the phase permutation has
`gcd(m,h)` cycles, proving item 1.  Every quotient row develops uniformly
over all phases, so it removes one unit from the orbit of `U_i` and adds one
to the orbit of `V_i`, proving (1.14).  Equality of two finite multisets of
free cap orbits is equivalent to matching their entries; choosing literal
representatives gives precisely (1.15). \(\square\)

There is a sharp obstruction to the most obvious retained-label rule.
Write

\[
 y_i=f_i\cup\{z_i\},qquad z_i\notin x_i\cup\rho^{a_i}x_{i+1}. \tag{1.16}
\]

Then `U_i=x_i+z_i` and `V_i=rho^{a_i}x_{i+1}+z_i`.  Under the natural cap
transport `pi(i)=i+1,q_i=a_i`, equation (1.15) is equivalent to

\[
                         z_i=\rho^{a_i}z_{i+1}.           \tag{1.17}
\]

Multiplying (1.17) around the circuit gives

\[
                         z_0=\rho^h z_0.                 \tag{1.18}
\]

If the coordinate action is free, (1.18) forces `h=0`.  Therefore a
coprime-voltage heptagon cannot use the naïve sequential fixed-label cap
rotor.  It must use at least one of:

1. a nontrivial cap permutation in (1.15);
2. duplicated old-cap tickets, so (1.14) remains positive without multiset
   equality; or
3. a larger compound return which closes the cap debt only at its terminal
   state.

The authenticated 2,822-to-2,754 witness uses the second/third mechanism:
its quotient holonomy is `h=5 mod 17`, while its cap multiset is not exact.

## 1.2 Twisted seven-step socket supply

Let `m=k` be odd and let `h` be coprime to `k`.  For a rank-`r` owner `X`,

\[
 d_J(X,\rho^hX)=|X\setminus\rho^hX|                     \tag{1.19}
\]

is the number of positive runs in the cyclic binary trace read in `h`-step
coordinate order.  Hence a quotient seven-row circuit with holonomy `h`
can be rooted at `X` only if this number is at most seven.

The number of rank-`r` owners with exactly `s` such runs is

\[
 \frac{k}{s}{r-1\choose s-1}{k-r-1\choose s-1}.          \tag{1.20}
\]

Indeed, distinguish one of the `s` one-run starts and record the positive
compositions of the `r` ones and `k-r` zeros into `s` parts.  There are `k`
choices for the distinguished start, and every owner is counted `s` times.

For `s=7`, choose any order of the seven deletions in
`X\setminus rho^hX` and any order of the seven insertions in
`rho^hX\setminus X`.  This gives `(7!)^2` geodesic seven-step moving paths
from `X` to `rho^hX`, hence quotient heptagons of voltage `h`.  If a fixed
coordinate `a` is required to be one of the seven deleted boundary labels,
the exact number of possible anchors is

\[
                  {r-1\choose6}{k-r-1\choose6},          \tag{1.21}
\]

which is `Theta(k^12)` in the central regime.  At each row, a retained
extension label has `k-r-1` raw choices outside the two adjacent owners; after
finitely many simplicity exclusions, `Omega(k)` remain.  Thus coprime-voltage
seven-step sockets are polynomially abundant for any fixed number of private
defect tasks, even though they form a negligible fraction of all central
owners.

To make this a complete immediate-upper packet, either solve the orbit
matching (1.15) or attach seven duplicate-cap backup tickets.  The latter is
only an `O(1)` interface, but planting it jointly with the path history is
part of the open host-spread lemma.

## 2. A one-cycle planting criterion

Assume a one-cycle factor contains the seven old edges.  Delete them and
suppose the retained paths can be oriented as

\[
 P_i:x_i\leadsto y_{i+1}.                                 \tag{2.1}
\]

The old factor traverses the paths in step-one order

\[
 P_0,P_1,P_2,\ldots,P_6.                                  \tag{2.2}
\]

### Theorem 2 (odd step-two rethread)

After (1.7), the terminal factor traverses the same oriented paths in
step-two order

\[
 P_0,P_2,P_4,P_6,P_1,P_3,P_5,                             \tag{2.3}
\]

and is one cycle.

More generally, the same statement with `t` paths gives `gcd(t,2)` terminal
components.  Every odd endpoint circuit satisfying (2.1) is therefore
topology-safe.

#### Proof

Path `P_i` ends at `y_{i+1}`.  Its new seam is
`y_{i+1}x_{i+2}`, the initial endpoint of `P_{i+2}`.  Thus the path index is
advanced by two.  The number of orbits of this addition map on `Z/tZ` is
`gcd(t,2)`. \(\square\)

### Corollary 2.1 (voltage development)

If a quotient heptagon under a free `Z_m` action has moving-owner voltage
`h`, put `g=gcd(m,h)`.  Its development has `g` moving circuits, each of row
length

\[
                              7m/g.                       \tag{2.4}
\]

When `m` is odd, these lengths are odd.  Therefore every developed module
whose retained paths satisfy the lifted form of (2.1) passes the step-two
one-cycle test.  In particular the uniform theory must allow both `h=0`
phasewise `C14`s and nonzero-voltage long returns.

This provides a literal sufficient topology row; it is not a claim that an
arbitrary incumbent factor exposes (2.1).

### Theorem 2.2 (seven-component cap-exact merger)

Suppose instead that the seven old edges `e_i=x_i y_i` of Theorem 1 lie on
seven distinct factor cycles.  Then toggling all seven rows to
`e_i'=y_i x_{i+1}` merges those seven cycles into one and leaves every other
component unchanged.  Both immediate palettes are preserved exactly.

#### Proof

Deleting one edge from each old component turns it into a path `Q_i` from
`x_i` to `y_i`.  The new edge `y_i x_{i+1}` concatenates

\[
 Q_0,Q_1,\ldots,Q_6
\]

cyclically into one component.  The palette assertion is Theorem 1. \(\square\)

Thus the fixed-`z` heptagon is not only a residence rethread: it is a
six-unit, cap-multiset-exact component absorber.  A resource-disjoint bank of
`H` such mergers reduces component count by `6H`.

For a given factor `F`, define its **heptagon connector hypergraph** to have
one vertex per component of `F` and one seven-edge hyperedge for every
cap-exact heptagon whose old rows lie on seven distinct components.  A
spanning sequence of such hyperedges would Hamiltonize the factor without
changing either immediate palette.  The exact obstruction is now a component
cut: a nontrivial component partition across which no legal heptagon exists.
Neither the protected two-factor extension theorem nor raw labelled count
rules out such a cut; proving expansion of this connector hypergraph is a
separate topology bridge.

## 3. The complete boundary-history state

Fix residence depth `d`.  For a binary path trace `P`, let

\[
 \Theta_d(P)                                               \tag{3.1}
\]

be its two truncated transfer maps, one for ones and one for zeros.  Each
map has states `0,1,...,d,d+1`: state zero means the previous symbol is the
opposite value, states `1,...,d` are the active run ages, and `d+1` means an
accepted long run.  A transition records both the outgoing state and the
number/deficit of completed short runs.  Store the transfer for both
orientations of `P`.

The seven-path **boundary history** is

\[
 \mathcal H=(\Theta_d(P_0),\ldots,\Theta_d(P_6)).          \tag{3.2}
\]

### Theorem 3 (exact clean-merger predicate)

Let `B_1(H)` and `B_2(H)` be the residence vectors obtained by composing
the transfers in the orders (2.2) and (2.3).  Then the exact residence drift
of the heptagonal circuit is

\[
                       B_2(\mathcal H)-B_1(\mathcal H).   \tag{3.3}
\]

All positive and zero runs strictly internal to the retained paths cancel.
Thus `H` is a componentwise nonworsening merger history iff (3.3) is
componentwise nonpositive, and it is a strict Pareto-improving history when
one declared coordinate is strict.  This is not by itself terminal
bi-residence: zero short-run debt additionally requires

\[
                              B_2(\mathcal H)=0.          \tag{3.3a}
\]

#### Proof

Both factors use every oriented retained path exactly once.  Only their
concatenation order differs.  The truncated automaton is Markov-sufficient
for the short-run count and deficit, so composing it in the two orders gives
the literal cyclic scans.  Subtraction cancels every internal charge. \(\square\)

For search and descent the appropriate accepting potential is at least

\[
 \Phi=(S_+,D_+,S_0,D_0),                                  \tag{3.4}
\]

with an explicitly declared lexicographic or weighted order.  Requiring
strict decrease of `S_+` at every primitive is too strong.  In the live
`k=17` trajectory, a `C12` at the 3,043 floor keeps `S_+` fixed while reducing
`D_+` by 17; a subsequent `C8+C6` return then unlocks the 3,009 factor.
Accordingly a bounded accepting chain may carry temporary component/cap or
primary-count debt, provided its terminal state passes every guard and has
negative total `Phi`-charge.

## 4. Exact prospective count through one rooted defect

Treat `(X,a)` as the private anchor of one defect task.  Keep the role names
in (1.1), so different role assignments are different prospective tickets.

### Theorem 4 (rooted heptagon count)

The number of labelled cap-exact heptagonal circuits rooted at `(X,a)` is

\[
 \boxed{
 N_{k,r}=(r-1)(r-2)(k-r)_4(k-r-4),
 }                                                            \tag{4.1}
\]

where `(n)_4=n(n-1)(n-2)(n-3)`.  In the central regime
`r=k/2+O(1)`, this is `Theta(k^7)`.

#### Proof

Choose the ordered internal roles `(b,c)` in `(r-1)(r-2)` ways, the ordered
external roles `(p,q,s,t)` in `(k-r)_4` ways, and `z` from the remaining
`k-r-4` coordinates outside `C` and the active labels.  The labelled data
recover (1.4)--(1.7), and every such choice is legal by Theorem 1. \(\square\)

This is a prospective count.  It is available while the host factor and its
off-state are selected; it is not a neighbourhood-size theorem for a frozen
literal factor.

## 5. Central-token load and bounded packet packing

The central token ledger of a heptagon consists of its seven moving owners,
seven retained owners, seven facets, seven caps, and fourteen old/new row
options.  Its common two-token skeleton is

\[
                     X,\qquad X\setminus\{a\}=f_6.       \tag{5.0}
\]

Both are part of the private rooted defect anchor.

### Lemma 5 (one-degree loss for every nonanchor token)

There is an absolute constant `K_0` such that any fixed token outside the
private anchor skeleton (5.0), of one of the types above, occurs in at most

\[
                         K_0 k^6                         \tag{5.1}
\]

rooted labelled tickets.

#### Proof

There are only finitely many role patterns in (1.4)--(1.10).  In every
nonanchor-skeleton pattern, equality with a fixed token determines at least one of
the seven free role values `(b,c,p,q,s,t,z)`: equivalently, the symmetric
difference with fixed `X` contains or omits a nonconstant role.  Choose the
pattern and the revealed role in `O(1)` ways, then choose the remaining six
roles in at most `k^6` ways. \(\square\)

### Corollary 6 (avoidance of a sublinear bank)

If a fixed forbidden central bank has size `B`, at most `O(Bk^6)` rooted
tickets meet it outside (5.0).  Hence, for `B=O(d)` and `d=o(k)`, a
`1-O(d/k)` fraction of the `Theta(k^7)` atlas survives.

Suppose in addition that every complete physical ticket uses `O(d)`
nonanchor history/occurrence resources and that each such resource also has
load `O(k^6)` in every other private-anchor atlas.  Then one selected packet
excludes only

\[
                         O(dk^6)                          \tag{5.2}
\]

options from another task.  Greedy selection therefore succeeds for `H`
private-anchor tasks whenever

\[
                         Hd=o(k).                         \tag{5.3}
\]

In particular it succeeds for every fixed `H` when
`d=Theta(sqrt(k))`.

The central-token part of this corollary is unconditional.  The same-load
claim for the complete history ticket is the remaining physical spread row.

For `k=17,r=9`, complete O3 enumeration of one rooted atlas gives exactly
376,320 labelled tickets, agreeing with (4.1).  After excluding the private
owner/facet skeleton (5.0), the maximum observed load of any moving-owner,
retained-owner, facet, or cap token is 47,040.  The same audit independently
finds 476 voltage-one owner anchors with seven runs and 196 such anchors
through a fixed coordinate boundary, exactly matching (1.20)--(1.21).  The
replay artifacts are

```text
scratch/audit_heptagonal_cap_circulation_atlas_20260802.cpp
scratch/k17_upper_decorated_longrun_circuit_20260802/
  heptagon_atlas_k17_r9.audit.json
```

with SHA-256 values

```text
c4dadda7fdfce8092a2a3fdf2b43f2a7c351674f464675b8cd626180c6ac8e65
2b58e7b2de4009198f5a2acf29f7b55ba76af51d5426f056c3b32c655a97f35b
```

## 6. Finite calibration and what it proves

The authenticated `k=17` 3,094-to-3,060 exchange is an endpoint `C14` with
seven quotient rows.  Its independent replay is

```text
scratch/k17_upper_decorated_longrun_circuit_20260802/
  longrun3060.audit.json
  longrun3060.trace.tsv
  longrun3060.moving_cycles.tsv
```

The seven-row physical representative has moving triples on a six-element
core exactly of the form (1.4).  Its retained extension labels are not all
equal, so the concrete cap closure mixes transport with available slack;
nevertheless the abstract fixed-`z` subfamily proves cap-exact closure for
every parameter.

The literal per-coordinate residence drift is

\[
       (\Delta S_+,\Delta D_+,\Delta S_0,\Delta D_0)
                         =(-2,-4,-3,-6).                  \tag{6.1}
\]

Thus the accepting boundary-history class is nonempty.  This is a finite
existence witness, not a proof that a positive fraction of the prospective
atlas receives such a history in all dimensions.

The same 3,094 floor also contains exactly one connected cap-multiset-exact
quotient `C14` in the complete 268-candidate terminal census.  Independent
replay gives

\[
 (\Delta S_+,\Delta D_+,\Delta S_0,\Delta D_0)
                         =(0,-34,+17,+34).                \tag{6.1b}
\]

Thus a completely cap-neutral heptagon can make genuine lexicographic
residence progress even when it does not immediately lower the primary run
count.  Its seven old and seven new cap orbits agree by a nontrivial
permutation, illustrating (1.15) rather than the sequential fixed-`z` rule.
The independently frozen artifacts are

```text
scratch/k17_upper_decorated_longrun_circuit_20260802/
  floor3094.c14_exactcap.factor.tsv
  floor3094.c14_exactcap.audit.json
  floor3094.c14_exactcap.trace.tsv
```

with SHA-256 values

```text
c844e03c1c6e64f7cabfb757750280f4b02257408cc2a396dc77a213ba44a17e
736dd1138573e18560d27641ab1c0324fce8d4c31953d74d1a6be5ee64f6fdc9
409ed3a622c85e3c84d301979a836a7752e6212f9ca001c89fd7afb3944fc6c6
```

An even stronger authenticated terminal exchange is the 2,822-to-2,754
quotient `C14`.  Its holonomy is `5 mod 17`; hence its seven facet orbits develop into
one moving-owner circuit of physical row length 119.  Independent replay
gives the per-coordinate drift

\[
                         (-4,-6,-4,-6),                   \tag{6.1a}
\]

so both positive and zero short-run counts fall by 68 and both deficits fall
by 102.  Of the seven quotient cap occurrences, four cap orbits are
transported.  Three old cap orbits are genuinely replaced by three new ones;
every net-removed cap has old load two.  Thus every load-one removal is
returned, while duplicate units fund the three orbit changes.  All
central/immediate palettes and one physical factor component are retained. The
artifacts are

```text
scratch/k17_upper_decorated_longrun_circuit_20260802/
  longrun2754.audit.json
  longrun2754.trace.tsv
  longrun2754.moving_cycles.tsv
```

with SHA-256 values

```text
46dda4f08412ecd06b58885d50c65e4b7227b7d5952a2acb3184af0c17a92ec3
31aa36f6fc4a2be2dfaf03819dd81cbd5df0bd626949f6641a6a78fb81f38eea
092ffad06b367b8e6c21f8a913fdd6529a1415b28aa69d8d4811a83664473e44
```

The later 3,009-to-2,992 `C10` independently has drift

\[
                         (-1,-2,+2,+3),                   \tag{6.2}
\]

and closes the last 17 rank-thirteen upper holes while retaining the central
and immediate palettes.  This is useful evidence that residence polarity and
deeper-upper progress must be optimized as a bounded accepting path, not as
four simultaneous monotone coordinates.  The deeper-upper assertion is a
separate audit and is not implied by the endpoint-circuit theorem.

There is also a decisive negative calibration on the surrounding route.
Across the authenticated residence floors from 3,502 down through 2,907,
the nonflat deadline-particle scalar remains approximately

```text
Phi = 48,432 ... 48,462,
G2  = 79 ... 94,
```

where the required `G2` value is 20,610.  Thus long-circuit residence descent
is distributed rethreading; it does not create the enormous clustered
nonflat particle bank needed by that alternative route.  The theorem's
intended terminal target remains a flat depth-three resident factor (or a
separately proved bounded sidecar), not a nonflat deadline-particle escape.

## 7. Exact remaining abundance/regeneration theorem

The local circuit, cap closure, topology criterion, prospective count, and
central-token spread are now explicit.  The uniform step still missing is:

> **Heptagon host-spread lemma.**  For a positive fraction of exposed short
> run defects in a recursively constructed upper-exact factor, a positive
> fraction of the `N_{k,r}` rooted heptagons can be planted with (i) path
> order (2.1), (ii) an accepting boundary history or a bounded accepting
> return, (iii) protected deeper-upper tickets, and (iv) complete physical
> history-resource load `O(k^6)`.

Together with (5.2), this lemma would give bounded-task regeneration by a
greedy argument.  A stronger all-task version with the corresponding global
conflict degree would support an LLL selection.

What is **not** proved is crucial: a frozen arbitrary factor need not expose
even one of the prospective seven-row hosts; q1 two-factor extension does not
force path order (2.1); and neither the source antecedent nor the lower
compiler follows from this central circuit.  The present gain is that the
missing theorem now has an explicit `Theta(k^7)` atlas and an `O(dk^6)`
candidate-conflict scale, giving the favorable ratio

\[
                    \Omega(k/d)=\Omega(\sqrt{k}).         \tag{7.1}
\]

The remaining issue is physical history supply, not central palette algebra
or raw labelled abundance.

# Unsaturated one-copy hinges: skeleton damage, two-switch expansion, and overlap sidecars

**Date:** 2026-08-02  
**Lane:** A, integral coloured rotors  
**Status:** exact connected-completion calculus and a deterministic positive
expansion theorem.  The hypotheses below must be checked on the literal
residence/upper-filtered menus; raw Boolean menu size does not imply them.

## 0. Outcome

For the one-sided hinges of
`MATH_THEOREM_A_UNSATURATED_ONECOPY_HINGE_AND_PROTECTED_COMPLETION_GATE_20260802.md`,
the protected head is fixed and all surviving freedom is in the predecessor
tail.  This note isolates the topology row after the ordinary predecessor
Hall theorem.

There are three exact conclusions.

1. Reserving a distinct-role forest consumes Hall slack by one explicit
   **menu-cut damage** function.  Thus the shifted Hoffman test has no hidden
   term, and only low-slack shores can obstruct an `O(1)` connector.
2. On the unit-capacity face, a concrete two-switch cut-expansion inequality
   turns every predecessor cycle cover into one protected Euler cycle.  A
   simpler row/column defect bound gives a readily checkable sufficient
   condition.
3. Even `O(1)` Euler components do not give an `O(1)` literal sidecar: the
   order-`d` overlap distance can be `d`.  Moreover the raw unsaturated menu
   construction admits physically literal separated-cycle banks, so neither
   connectedness nor bounded reset follows from unsaturation alone.

The live all-`k` gate is therefore an expansion theorem for one specifically
chosen, fully protected chain table, or a protected multi-edge macro which
crosses the low-slack shores described below.

## 1. Fixed-head protected predecessor data

Let `V` be the finite set of complete literal interface states.  A state
contains the order-`d` tuple, clipped signed run histories, endpoint marks,
and the boundary signature needed by the named upper-witness bank.

Let `I` be the free roles.  Role `i` has a fixed completed head `h_i in V`
and a nonempty accepted predecessor menu `M_i subseteq V`.  For every
`a in M_i`, the packet `a -> h_i` has the same owner, named lower payload,
and protected upper tickets, and passes the literal internal residence and
exterior-signature audits.  Let `P` be the fixed protected bank and put

\[
 \eta=\partial P,\qquad
 m(v)=|\{i:h_i=v\}|,\qquad b(v)=m(v)+\eta(v).       \tag{1.1}
\]

The exact free-tail demand is `b`.  Hence assume `b>=0` and
`b(V)=|I|`.  For `X subseteq V`, define

\[
 \ell(X)=|\{i:M_i\subseteq X\}|,
 \qquad \sigma(X)=b(X)-\ell(X).                     \tag{1.2}
\]

The fixed-head Hoffman theorem says precisely that a protected predecessor
selection exists iff

\[
                         \sigma(X)\geq0\quad(X\subseteq V). \tag{1.3}
\]

Equivalently, for every role set `J`,
`|J|<=b(union_(i in J) M_i)`.  It suffices to test unions of accepted menus.
Nothing in this note replaces the requirement that the `M_i` were obtained
by literal residence and upper-witness filtering.

## 2. The exact skeleton-damage identity

Reserve packets

\[
                         R=\{(i,a_i):i\in I_R, a_i\in M_i\}, \tag{2.1}
\]

from pairwise distinct roles.  Write

\[
 t_R(v)=|\{i\in I_R:a_i=v\}|,
 \qquad b_R=b-t_R.                                  \tag{2.2}
\]

For a shore `X`, define

\[
 D_R(X)=|\{i\in I_R:a_i\in X\text{ and }M_i\not\subseteq X\}|. \tag{2.3}
\]

Thus a reserved role damages `X` exactly when its selected tail is in `X`
but its menu has an alternative outside `X`.

### Theorem 2.1 (shifted Hoffman equals menu-cut damage)

After reserving `R`, the residual predecessor table is feasible if and only
if `b_R>=0`, every residual menu is nonempty on the intended state support,
and

\[
                         \boxed{D_R(X)\leq\sigma(X)}            \tag{2.4}
\]

for every `X subseteq V`.  It again suffices to test sets which are unions
of residual menus.

Consequently, if the underlying undirected support of `P union R` spans the
intended state set with at most `c` components, (2.4) is an exact
at-most-`c` protected Euler certificate.  For `c=1` it is an exact
zero-route-sidecar certificate.

#### Proof

Deleting the reserved roles changes the number of menus contained in `X`
to

\[
 \ell_R(X)=\ell(X)-|\{i\in I_R:M_i\subseteq X\}|.   \tag{2.5}
\]

The residual Hall slack is therefore

\[
 \begin{aligned}
 b_R(X)-\ell_R(X)
 &=\sigma(X)-|\{i\in I_R:a_i\in X\}|
   +|\{i\in I_R:M_i\subseteq X\}|\\
 &=\sigma(X)-D_R(X),                                \tag{2.6}
 \end{aligned}
\]

because `M_i subseteq X` implies `a_i in X`.  The fixed-head Hall theorem
now gives (2.4), including the reduction to unions of residual menus.
Adding the reserved forest to the residual balanced selection proves the
component assertion.  Conversely, a spanning forest extracted from any
completed solution supplies such an `R`, and its residual selection proves
(2.4).  \(\square\)

### Corollary 2.2 (finite low-slack separator)

If `|R|=t`, then `D_R(X)<=t`; hence only shores with
`sigma(X)<t` can reject `R`.  In particular, on every tight shore
`sigma(X)=0`,

\[
 a_i\in X\quad\Longrightarrow\quad M_i\subseteq X
 \qquad(i\in I_R).                                 \tag{2.7}
\]

If the protected bank already has `c=O(1)` spanning components, only
`c-1` connector roles are needed, and the complete obstruction library is
the finite family of residual-menu unions with slack at most `c-2`.

Equation (2.7) is one-sided.  A reserved packet entering `X` through its
fixed head costs no tail capacity inside `X`; a packet selected at a tail in
`X` costs one unless its whole menu is trapped there.

### Corollary 2.3 (tight-shore topology obstruction)

Let `sigma(X)=0`, and suppose the protected support has a component on each
side of `X`.  If every accepted packet crossing the shore has its selected
tail `a in X`, its fixed head outside `X`, and a menu which is not contained
in `X`, then no connected protected completion exists.

Indeed every spanning forest must contain a shore-crossing packet, while
every such packet contributes one to `D_R(X)` and violates (2.4).  The
hypothesis deliberately excludes a packet entering `X` from an outside
tail: such an incoming packet has zero damage on `X` and is a genuine
one-sided escape.

## 3. Exact two-switch fusion criterion

Now specialize to the unit-capacity face:

* `I=V`, with role `i` having fixed head `i`;
* `P` is balanced at the state projection, so `b(v)=1`; and
* every accepted packet in `M_i times {i}` carries the same protected
  role payload.

A predecessor selection is a permutation `p` of `V`, where
`p(i) in M_i`; its selected arc is `p(i) -> i`.  Its Euler components are
the cycles of that permutation support.

For `C subset V`, put

\[
 \begin{aligned}
 \mathcal D(C)=
 &\sum_{i\in C}|(V-C)-M_i|\\
 &+\sum_{j\in V-C}|C-M_j|.                          \tag{3.1}
 \end{aligned}
\]

Here `A-B` denotes set difference.

### Theorem 3.1 (two-switch cut expansion)

Assume the predecessor Hall cuts hold and

\[
 \boxed{\mathcal D(C)<|C|\,|V-C|}
 \qquad(\varnothing\ne C\subsetneq V).             \tag{3.2}
\]

Then there is a protected one-cycle predecessor selection.  More strongly,
starting from any predecessor cycle cover, a sequence of legal protected
two-switches decreases the number of components by one at every step.

#### Proof

Let `p` be a current cycle cover and let `C` be the vertex set of one or
more, but not all, of its cycles.  Thus `p(C)=C` and `p(V-C)=V-C`.

Suppose no roles `i in C`, `j in V-C` admit the mutual exchange

\[
                         p(j)\in M_i,qquad p(i)\in M_j.       \tag{3.3}
\]

For each of the `|C||V-C|` ordered cross pairs `(i,j)`, at least one
condition in (3.3) then fails.  Since `p` permutes `C` and `V-C`
separately, the number of first failures is exactly

\[
                         \sum_{i\in C}|(V-C)-M_i|,
\]

and the number of second failures is exactly

\[
                         \sum_{j\in V-C}|C-M_j|.
\]

Their sum must be at least `|C||V-C|`, contradicting (3.2).  Hence (3.3)
holds for some cross pair.  Swap the two assigned tails:

\[
 p(i)\to i, p(j)\to j
 \quad\longmapsto\quad
 p(j)\to i, p(i)\to j.                            \tag{3.4}
\]

The two new arcs are accepted, every tail and head is still used once, and
the rolewise protected payloads are unchanged.  Cutting one arc from two
different cycles and crossing their heads merges the cycles.  Condition
(3.2) is independent of `p`, so the argument repeats until one cycle
remains.  \(\square\)

The failure certificate for this method is exact: a cycle cover is
two-switch locked across a union `C` of its cycles precisely when every
cross pair is covered by one of the two rejection relations in (3.3).
This is a semantic occurrence-labelled obstruction, not a mask-degree
shortcut.  It does not exclude a larger `q`-switch.

### Corollary 3.2 (dense accepted-menu criterion)

Let `N=|V|` and define

\[
 \rho=\max_i|V-M_i|,
 \qquad
 \kappa=\max_v|\{i:v\notin M_i\}|.                 \tag{3.5}
\]

If predecessor Hall holds and

\[
                         \rho+\kappa<N/2,            \tag{3.6}
\]

then a protected one-cycle selection exists.

#### Proof

For any current cycle cover, join roles `i,j` in its exchange graph when
(3.3) holds.  At most `rho` roles `j` fail its first condition and at most
`kappa` fail its second, so every exchange-graph vertex has degree at least
`N-1-rho-kappa>=floor(N/2)`.  Such an undirected graph is connected: a
smallest component would have at most `floor(N/2)` vertices and hence
maximum internal degree at most `floor(N/2)-1`.  Therefore, whenever the
cycle cover has more than one component, an exchange edge joins two of
them.  Apply (3.4) and iterate.  \(\square\)

The Boolean interval size `2^(|S_1|-1)` does not by itself imply (3.2) or
(3.6).  The tails must also occur broadly and with bounded rejection load
in the chosen global head bank after every residence and upper filter.

## 4. Literal overlap distance and the sidecar gap

For order-`d` literal states

\[
 u=(u_1,\ldots,u_d),\qquad v=(v_1,\ldots,v_d),
\]

define

\[
 \operatorname{ov}(u,v)=
 \max\{q:0\leq q\leq d,
       (u_{d-q+1},\ldots,u_d)=(v_1,\ldots,v_q)\},    \tag{4.1}
\]

and

\[
                         \delta_d(u,v)=d-\operatorname{ov}(u,v). \tag{4.2}
\]

### Proposition 4.1 (chronology-only reset lower bound)

Every literal de Bruijn path from `u` to `v` appends at least
`delta_d(u,v)` new letters, and equality is attained by appending the
unmatched suffix of `v`.  Therefore any sidecar which joins Euler
components through exits `u_t` and entries `v_t` has chronology length at
least the corresponding directed overlap-routing cost.

This is only a chronology lower bound.  The equality path need not preserve
owners, named palettes, residence, upper witnesses, or compiler rows.

#### Proof

After appending `s<d` letters, the final state retains the last `d-s`
letters of `u`; equality with `v` therefore requires a suffix-prefix
overlap of length at least `d-s`.  This gives `s>=delta_d(u,v)`.  Appending
the final `delta_d(u,v)` letters of `v` realizes equality.  \(\square\)

In particular, two states with no literal suffix-prefix overlap require
`d` reset letters.  Thus `O(1)` components imply an `O(1)` sidecar only if
the selected component ports have `O(1)` total overlap-routing cost (and
the required physical resources exist).  Component count alone is
insufficient.

## 5. A literal separated-cycle obstruction

The following family shows why the expansion hypothesis is substantive.
Fix `d>=2` (so the owner rank `d+1` is at least three) and take two disjoint
alphabets

\[
 \{a_0,\ldots,a_{L-1}\},\qquad
 \{b_0,\ldots,b_{L-1}\},\qquad L\geq d+2.           \tag{5.1}
\]

For each `t modulo L`, make an `a`-role whose full trace is

\[
 (\{a_t\},\{a_{t+1}\},\ldots,\{a_{t+d}\}).         \tag{5.2}
\]

Declare the last `q` singleton letters to have union `S_(t,q)` for
`1<=q<=d`.  Its owner is the `(d+1)`-set of all letters in (5.2), and its
fixed head is the final `d`-tuple.  This is exactly the `ell=d` case of the
unsaturated hinge with `S_1={a_(t+d)}`.  Hence its guard exhausts `S_1` and
its predecessor menu is the singleton consisting of the first `d`-tuple,
which is the preceding fixed head.  Define the `b`-roles analogously.

All owners and all named suffix targets are distinct within a bank, and the
two disjoint alphabets keep them distinct across banks.  The fixed-head
Hall cuts hold with equality, but the selected predecessor factor is forced
to be exactly two cycles.  There is no completed-hinge fusion because every
menu is a singleton.  States in different banks have overlap zero, so any
literal cross-bank reset has length at least `d` by Proposition 4.1.

This example is an exact owner/payload and de Bruijn-topology obstruction.
It deliberately does **not** claim that the raw singleton traces satisfy a
separately imposed all-coordinate residence or upper-witness specification.
Its force is the scoped one needed here: unsaturated owner legality and
ordinary predecessor Hall do not imply protected connected completion or
an `O(1)` sidecar.  Any positive all-`k` theorem must use the additional
residence/upper-filtered expansion of its chosen Boolean table.

At depth one, the distinct-owner four-role Hall obstruction in
`MATH_THEOREM_A_UNSATURATED_HINGE_PREDECESSOR_HALL_AND_BOOLEAN_INTERVAL_OBSTRUCTION_20260802.md`
already shows that even ordinary matching need not exist.  The separated
cycles above are instead designed to isolate the topology and overlap rows
after matching is exact.

## 6. Exact remaining gate

There are now two proof-safe routes from one-sided hinges to a protected
Euler carrier.

1. **Skeleton route.**  Construct a distinct-role forest `R` spanning the
   protected components and prove the finite low-slack inequalities
   `D_R(X)<=sigma(X)` on residual-menu unions.
2. **Exchange route.**  First solve predecessor Hall, then prove the
   occurrence-labelled two-switch expansion (3.2), or an analogous
   protected `q`-switch expansion, and fuse adaptively.

For `O(1)` sidecar it is additionally necessary to exhibit ports whose
total literal overlap-routing cost is `O(1)`.  Neither the corrected
stationary pull clock nor raw Boolean menu cardinalities provide these
properties.  The missing positive statement is a joint spread theorem for
accepted predecessor occurrences, not another fractional marginal theorem.

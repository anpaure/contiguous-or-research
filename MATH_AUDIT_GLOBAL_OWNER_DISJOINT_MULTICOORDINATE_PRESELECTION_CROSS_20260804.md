# Cross-audit: global-owner-disjoint multicoordinate preselection

**Date:** 2026-08-04  
**Method:** independent symbolic audit only; no search, finite experiment,
or computational construction.

**Audited theorem:**
`MATH_THEOREM_GLOBAL_OWNER_DISJOINT_MULTICOORDINATE_PRESELECTION_20260804.md`,
SHA256
`fab1d624778ddf687867fad2969d5821a3383dd38f8e6da7e5e26d571f4a69f9`.

## 0. Verdict

PASS.  The global-deletion Hall inequality, the endpoint reduction, the
simple sufficient rows, and the protected-factor collision ledger are all
correct.  The result is complementary to the turn-diamond router: it removes
owner aliases for a small simultaneously required multicoordinate bank,
whereas the turn-diamond theorem resolves aliases by selecting only one of
the two factor incidences per claim.

## 1. Global-deletion Hall bound

At stage `q`, the already selected owner bank is

\[
 R_q=\{\mu_t(i):t<q, i\in I\}.
\]

Inductive global disjointness gives `|R_q|=qp`, and every earlier selection
avoids `F`, so

\[
                         |F\cup R_q|=f+qp.
\tag{1.1}
\]

For `X subseteq I`, `|X|=x`, the injected lower sets are distinct.  Two
distinct rank-`m-1` lower sets have at most one common rank-`m` upper
neighbour, since any common neighbour must equal their union.  Bonferroni's
first lower bound therefore gives

\[
 \left|\bigcup_{i\in X}A_i^q\right|
 \ge xL_q-{x\choose2}.
\tag{1.2}
\]

Deleting the entire previous owner bank and the fixed forbidden bank can
remove at most `f+qp` values from this union.  Hence

\[
 \left|\bigcup_{i\in X}
    \bigl(A_i^q\setminus(F\cup R_q)\bigr)\right|
 \ge xL_q-{x\choose2}-f-qp.
\tag{1.3}
\]

Hall requires the right side to be at least `x`, equivalently

\[
 Q_q(x)=x(L_q-1)-{x\choose2}-f-qp\ge0.
\tag{1.4}
\]

As a real quadratic, `Q_q` is concave.  Its minimum on `[1,p]` is at an
endpoint.  The two endpoint conditions are exactly

\[
 f+qp\le L_q-1,
 \qquad
 p(L_q-1)-{p\choose2}-f-qp\ge0.
\tag{1.5}
\]

Thus the induction produces a new matching avoiding every previously used
owner, and all `cp` selected owners are globally distinct.

The subtraction of `qp` is deliberately global and may be conservative:
it does not assume which old owners lie in a particular new menu.  Therefore
there is no hidden menuwise independence premise.

## 2. Audit of the simple sufficient rows

Put `F_q=f+qp`.  The simple hypotheses are

\[
 p\le L_q,
 \qquad
 F_q\le L_q-1.
\tag{2.1}
\]

The first endpoint follows immediately:

\[
                         Q_q(1)=L_q-1-F_q\ge0.
\]

For the other endpoint,

\[
\begin{aligned}
 Q_q(p)
 &\ge p(L_q-1)-{p\choose2}-(L_q-1)\\
 &=(p-1)\left(L_q-1-{p\over2}\right).
\end{aligned}
\tag{2.2}
\]

For `p=1`, the first endpoint already applies.  For `p>=2`, `p<=L_q`
implies

\[
 L_q-1-{p\over2}
 \ge {p\over2}-1\ge0.
\]

Hence the displayed simple rows do imply every exact Hall row.

## 3. Two-coordinate collision ledger

For `c=2`, each `mu_q` is a matching and global disjointness makes the two
coordinate images disjoint.  Consequently:

* the two selected edges at each injected lower vertex are distinct, so
  its selected degree is exactly two;
* every selected upper owner has degree exactly one in the new bank; and
* all `2p` selected edges are distinct.

Thus

\[
 |E(M)|=2p,
 \qquad d_M(\iota(i))=2,
 \qquad d_M(U)\le1.
\tag{3.1}
\]

After protected two-factor completion, occurrence serialization preserves
those exact loads: lower source two, owner cell at most one, edge halfport
one.  An incumbent bank `P_*` can still meet a selected owner, which is why
the theorem correctly retains the full degree condition on `P_* union M`.

The asymptotic statement is also exact for fixed `c`: if `p,f=O(sqrt(k))`
and every `L_q=Theta(k)`, then `p<=L_q` and `f+qp<=L_q-1` eventually.

## 4. Relation to the turn-diamond router

There is no overlap contradiction.

### One coordinate

The turn-diamond theorem starts with both factor incidences as alternatives
for one claim.  A component bit selects one alternating owner transversal,
so every owner alias has selected load one.  It does not need global
owner-disjoint preselection, but it routes only one ticket per claim and
uses the claim's q1 upper-turn occurrence as its canonical terminal.

### Two or more simultaneous coordinates

When all coordinate tickets are conjunctively required, unused alternatives
cannot absorb an alias.  Global owner-disjoint preselection gives exactly

\[
                         d_M(U)\le1
\]

for the complete new bank, eliminating the shared owner-cell gate without
postselection.  This is the right repair for a small protected bank.

It cannot extend to two copies of the full factor shore: `2|mathcal L|`
distinct owner selections do not fit in the `|mathcal U|=|mathcal L|`
owner set.  Equivalently, the turn-diamond owner shore is a cut of capacity
`|mathcal U|` for twice as many full-shore demands.  The two theorems agree
on this boundary.

## 5. Exact combined router frontier

The combined pure-mathematical state is now:

1. **One chosen incidence per claim.**  Factor serialization plus the
   canonical turn diamond resolves halfport-to-owner aliasing by one
   component parity bit.  If its source, owner, and q1 upper-turn occurrence
   are active, unused, and typed in one cap state, it is already a private
   literal route; no full-port suffix rank is needed.
2. **Several simultaneously required coordinate tickets.**  Sequentially
   deleting every earlier owner bank gives globally owner-disjoint selected
   incidences under the audited Hall rows.  Owner-cell capacity is then
   exact with load one.
3. **Still open in both cases.**  Factor/preselection does not activate the
   selected occurrence nodes after compensation, provide `c` physical
   source units at one lower turn, create distinct typed terminal capacities,
   or prove cross-coordinate product closure.  If the q1 upper-turn cell is
   not itself a legal free sink, a one-step Boolean or more general typed
   suffix router remains necessary.
4. **Canonical two-coordinate warning.**  The two turn-diamond branches at
   one lower turn end at the same unit q1 upper-turn occurrence.  Removing
   owner aliases alone therefore does not route both tickets: terminal
   occurrence splitting, capacity two, or two different typed sinks is
   still required.

Accordingly the new Hall theorem exactly removes the selected-bank owner
alias row.  It does not close source multiplicity, cap activation, suffix
typing, terminal multiplicity, or product closure.


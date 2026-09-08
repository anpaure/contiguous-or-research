# Independent audit of the proposed `k=11` local-density theorem

## 1. Verdict

The two unrestricted local-density statements are correct:

\[
  p_Y:=|\{i:A_i\subseteq Y\}|\ge 16
  \quad\text{for every }Y\in\binom{[11]}5,
\]

and

\[
  p_U:=|\{i:A_i\subseteq U\}|\ge 23
  \quad\text{for every }U\in\binom{[11]}6.
\]

The resulting averaged inequalities are also correct:

\[
 \sum_{i:|A_i|\le5}\binom{11-|A_i|}{5-|A_i|}\ge7392,
 \tag{1}
\]

\[
 \sum_{i:|A_i|\le6}\binom{11-|A_i|}{6-|A_i|}\ge10626.
 \tag{2}
\]

They are genuinely new relative to `MATHEMATICAL_HANDOFF.md` and
`K11_INTEGRATED_SEARCH.md`.  Section 8.4 of the integrated search contains
the weaker dimension-restriction bounds `p_Y>=nu(5)=12` and
`p_U>=nu(6)=21`, together with their averages.  The new argument strengthens
these to 16 and 23 by using the **global length-four barrier** forced at the
hypothetical optimum `n=465`.

The conditional coordinate-crossing calculation for a fixed Johnson
Hamilton row is also correct.  It is not the same as the general Catalan
balance laws already recorded in Sections 43 and 74 of the handoff.  However,
it applies only to the fixed-row ansatz and is already logically implied by
the vertex and intersection-colour constraints of that ansatz.  The sentence
that the value 84 “explains” a 42-component decomposition is motivation, not
a consequence of the displayed calculation: a coordinate crossing count is
not by itself a component count.

The numerical search status in the supplied text is stale.  The present
verified bounds are

\[
  465\le\nu(11)\le477,
  \qquad 466\le N(11)\le478,
\]

using `k11_completed_477.txt`, not `nu(11)<=508` and `N(11)<=509`.

## 2. Audit of the common length-four barrier

Choose one witness for each of the 462 six-sets.  At length

\[
  465=\binom{11}{6}+3,
\]

the standard nonnesting argument places the `i`-th selected witness inside
`[i,i+3]`.  Every physical interval of length at least four contains one of
these selected witnesses and consequently has OR-rank at least six.

There is no endpoint error here.  If `J=[a,b]` has length at least four, then
`b>=a+3`; since `b<=465=462+3`, one has `a<=462`, and the selected interval
`I_a` lies inside `[a,a+3]`, which lies inside `J`.

It follows that every mask of rank at most five has a witness of length at
most three.  This conclusion is unrestricted: it uses neither a derivative
row nor a Johnson path.

## 3. Audit of the five-set bound

Fix a five-set `Y` and mark the positions satisfying `A_i subseteq Y`.
They split into consecutive runs.  A run cannot have length four, because
four consecutive entries contained in `Y` would form a length-four interval
of OR-rank at most five.  Hence every run has length at most three.

A run of length `ell=1,2,3` contains respectively `1,3,6` intervals, and

\[
  \binom{\ell+1}{2}\le 2\ell.
\]

Every one of the 31 nonempty subsets of `Y` has a witness wholly inside these
runs: if an interval has union `S subseteq Y`, every entry of that interval
is itself contained in `S`, hence in `Y`.  Different target masks require
different physical intervals.  Therefore

\[
  31\le2p_Y,
\]

which gives `p_Y>=16`.  All inequalities and the rounding are correct.

Double counting the pairs `(i,Y)` with `A_i subseteq Y` gives (1), because an
entry of rank `s<=5` is contained in exactly

\[
  \binom{11-s}{5-s}
\]

five-sets.  Since `16*binom(11,5)=16*462=7392`, the right side is correct.
In entry-rank-count notation `n_s=|{i:|A_i|=s}|`, (1) is

\[
  210n_1+84n_2+28n_3+7n_4+n_5\ge7392.
  \tag{3}
\]

## 4. Audit of the six-set bound

Fix a six-set `U`.  Its 62 nonempty proper subsets all have rank at most five,
so each has a witness of length at most three, wholly among positions with
`A_i subseteq U`.

For `p>=3` marked positions split into runs, the number of contained intervals
of lengths one, two, or three is at most `3p-3`; merging runs cannot decrease
this maximum.  Thus

\[
  62\le3p_U-3,
\]

and initially `p_U>=22`.

The exclusion of equality is sound.  If `p_U=22`, two or more runs give at
most

\[
  (3\cdot21-3)+1=61
\]

short intervals, so all 22 positions form one block.  That block has exactly
`22+21+20=63` intervals of lengths at most three.  Sixty-two of them realize
the 62 distinct nonempty proper subsets of `U`; the remaining value is one
additional nonempty set `E subseteq U`.

Fix `b in U`.  Exactly 31 nonempty proper subsets of `U` contain `b`, so the
number `Z_b` of the 63 short windows whose OR omits `b` is

\[
  Z_b=32-1_{b\in E}.
  \tag{4}
\]

In the length-22 binary occurrence word for `b`, a zero-run cannot have
length four.  If `alpha,beta,gamma` count zero-runs of lengths one, two, and
three, then

\[
  Z_b=\alpha+3\beta+6\gamma,
  \tag{5}
\]

while separation of the runs inside 22 positions gives

\[
  2\alpha+3\beta+4\gamma\le23.
  \tag{6}

If `Z_b=32`, (5)--(6) imply

\[
  3\beta+8\gamma\ge41,
  \qquad 3\beta+6\gamma\le32.
\]

Thus `gamma>=5`; the only arithmetically possible case is
`gamma=5,beta=0,alpha=2`, and it violates (6) with left side 24.  Therefore
`Z_b=31`, so every `b` belongs to `E`, and `E=U`.

Solving (5)--(6) with `Z_b=31` gives uniquely

\[
  (\alpha,\beta,\gamma)=(1,0,5).
\]

Hence each coordinate occurs in exactly six of the 22 entries, and the sum
of their ranks is 36.  On the other hand, `E=U` means that all 63 short-window
OR values are the 63 nonempty subsets of `U`, each exactly once.  In
particular the 22 singleton-window values are distinct.  Each of the six
one-element masks must occur as a literal entry: a longer interval with OR
`{b}` would consist only of entries `{b}` and would duplicate that OR on a
singleton window.  The remaining 16 distinct entries have rank at least two,
so the rank sum is at least

\[
  6+2\cdot16=38,
\]

contradicting 36.  Therefore `p_U>=23`.

Double counting `(i,U)` gives (2), since an entry of rank `s<=6` belongs to
`binom(11-s,6-s)` six-sets and `23*462=10626`.  In rank-count notation this
is

\[
  252n_1+126n_2+56n_3+21n_4+6n_5+n_6\ge10626.
  \tag{7}
\]

## 5. Relation to inherited dimension cuts and band/fan cuts

The inherited dimension restriction says that for every `q`-set `Q`, at
least `nu(11-q)` entries avoid `Q`.  Taking complements:

* `|Q|=6` gives `p_Y>=nu(5)=12`; the new theorem gives 16.  Its averaged
  inequality has exactly the same left side as (3), but raises the right side
  from `12*462=5544` to 7392.
* `|Q|=5` gives `p_U>=nu(6)=21`; the new theorem gives 23.  Its averaged
  inequality has exactly the same left side as (7), but raises the right side
  from `21*462=9702` to 10626.

Thus the new inequalities strictly dominate these two inherited averaged
dimension cuts.

They do **not** dominate the monotone-band/fan inequalities, nor are they
dominated by them.  The band cuts constrain the widths of the 462 selected
rank-six witnesses (`x_0,...,x_3`); (3) and (7) constrain the ranks of the 465
literal entries.  These are different projections of the exact formula.

They are unlikely to help the structured fixed-row checkpoint.  The known
465-entry partial factor has rank distribution

```text
n1=75, n2=215, n3=175,
```

so its two left sides are respectively 38,710 and 55,790, far above 7,392
and 10,626.  Direct enumeration gives `min_Y p_Y=72` and `min_U p_U=109`.
The cuts may nevertheless prune high-rank literal assignments in the fully
unrestricted forest formula, where the current band/fan cuts say little about
entry ranks.

## 6. Audit of the conditional coordinate-crossing law

Assume a Johnson Hamilton path through all 462 six-sets, with its 461
adjacent intersections distinct and hence equal to all but one five-set.  For
a coordinate `z`, there are 252 vertices containing `z` and 210 avoiding it.
Let `a,b,c` count edges internal to the containing class, internal to the
avoiding class, and crossing between them.

An edge intersection contains `z` exactly when both endpoints contain `z`.
If the omitted five-set avoids `z`, all 210 five-sets containing `z` occur,
so `a=210` and `b+c=251`.  The two class-degree inequalities

\[
  2a+c\le504,
  \qquad 2b+c\le420
\]

give `82<=c<=84`.

If the omitted five-set contains `z`, then `a=209`, `b+c=252`, and the same
calculation gives `84<=c<=86`.  The off-by-one values are correct.  More
precisely, if `e_1` and `e_0` are the numbers of the two global path endpoints
in the containing and avoiding classes, then

\[
\begin{array}{c|c}
z\notin\text{omitted colour}&c=84-e_1=82+e_0,\\
z\in\text{omitted colour}&c=86-e_1=84+e_0,
\end{array}
\]

with `e_0+e_1=2`.  This is a useful checksum and a possible redundant
propagation cut for fixed-row path SAT.  It is not an unrestricted theorem,
and `c=84=2*Cat_5` alone does not prove the existence of 42 path components.

## 7. Recommended encoding

### 7.1 Cheap first experiment: the two averaged PB cuts

For every position `i`, derive an exact one-hot rank indicator
`R_(i,s) <-> (|A_i|=s)` for `1<=s<=11`.  Add (3) and (7) directly in a PB
solver, or encode them in CNF with a balanced binary-adder tree and an exact
unsigned comparator.  The rank circuit is shared by both inequalities.

This is the recommended first guard.  A binary-adder implementation should
cost only on the order of tens of thousands of variables and at most a few
hundred thousand clauses, small beside the current approximately
2.9-million-variable / 14.7-million-clause unrestricted branches.  It will
have weaker propagation than a unary weighted totalizer, but it is cheap and
easy to audit.  Exact inventory must of course be reported from the frozen
implementation rather than inferred from this estimate.

### 7.2 Strong form: selected local subcube cuts

For a fixed five- or six-set `S`, introduce

\[
  C_{i,S}\leftrightarrow\bigwedge_{b\notin S}\neg A_{i,b}
\]

and enforce `sum_i C_(i,S)>=16` or `>=23`.  These are the actual local-density
theorems and propagate physical containment, unlike their averages.

Eagerly encoding all 924 sets is probably too expensive for the present
solver.  The containment definitions alone use 429,660 auxiliaries and about
2,792,790 clauses.  A straightforward truncated dynamic-programming counter
would add roughly

```text
462*465*16 = 3,437,280 states for the five-set cuts,
462*465*23 = 4,941,090 states for the six-set cuts,
```

before their clauses.  This would be comparable to or larger than the whole
current formula.

A better engineering order is:

1. add the two cheap averaged guards;
2. benchmark a small symmetry-balanced sample of local five-/six-set cuts;
3. only if they materially reduce conflicts, implement a shared cardinality
   network or a native/external PB propagator for all 924 constraints.

The local cuts are redundant consequences of the exact universality formula,
so post-SAT lazy checking cannot reveal a violating full model.  Their only
purpose is earlier propagation; they must be present during search (or in a
genuine partial-assignment propagator) to help.

### 7.3 Conditional Catalan counter

For a fixed-row search with the omitted five-colour already canonical, define
the 461 adjacent-coordinate XORs and constrain their sums to the appropriate
three-value ranges above, or to the exact endpoint-refined value.  This is a
valid redundant checksum.  It should not be added to the unrestricted
forest/band solver, and it is lower priority than the averaged local-density
guard because the existing fixed-row vertex and colour constraints already
imply it exactly.

## 8. Final status

The supplied text contains one substantive new unrestricted contribution:
the two local-density bounds and their stronger averaged dimension cuts.
They do not solve `k=11`, and they are very slack on the best fixed-row
factor, but they are mathematically valid and expose a new literal-entry
projection for the unrestricted SAT search.

The rank-count proof and the statement that `nu(k)=B(k)` is conjectural are
already in the ledger.  The old upper bound 508/509 must not be copied into
the current handoff; the certified completion gives 477/478.

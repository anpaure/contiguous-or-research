# Two-component pin localization in the `k=11` Type-II branch

## 1. Verdict

There is a small, exact, coordinate-sensitive consequence of the laminar
pin-capacity theorem.  It is now available under a dedicated optional guard
in the production `k=11` encoding.

Assume a length-465 word is in the no-literal-six-set branch and that deleting
its literal five-set entries leaves two rank-at-most-four components.  Call
the slack-one component `C_1` and the slack-two component `C_2`.  If

\[
 V_i=\bigcup_{p\in C_i}A_p,\qquad D_i=[11]\setminus V_i,
\]

then every lower target which meets `D_2` is forced to occur **literally** in
`C_1`.  Consequently

\[
 \#\{p\in C_1:|A_p|=s\}
 \ge \binom{11}{s}-\binom{11-|D_2|}{s}
 \quad(1\le s\le4).                                    \tag{1.1}
\]

In particular,

\[
 \boxed{|D_2|\le2.}                                    \tag{1.2}
\]

Thus, if the coordinate-complete component is the slack-one component, the
other component contains at least nine of the eleven coordinates.  More
precisely, if `z` is the number of literal five-set positions, then

\[
\begin{array}{c|c}
z&|D_2|\\ \hline
1\le z\le31&|D_2|\le2,\\
32\le z\le96&|D_2|\le1,\\
97\le z\le134&|D_2|=0.
\end{array}                                             \tag{1.3}
\]

This is not another support average.  It names the physical component in
which an entire coordinate-indexed Boolean family must occur as literal
cells.

## 2. Exact two-component setup

The audited rank-filtration theorem gives the following facts in the Type-II
two-component branch.

* Every entry has rank at most five.
* All literal five-set occurrences are distinct; write their number as `z`.
* Deleting them leaves two nonempty components `C_1,C_2`.
* Independently choose one witness for every nonliteral five-set.  If `q_i`
  selected witnesses lie in `C_i` and `n_i=|C_i|`, the two positive slacks

  \[
  t_i=n_i-q_i
  \]

  are `{1,2}`.
* At least one of `V_1,V_2` is `[11]`.

Orient the component names so that

\[
t_1=1,\qquad t_2=2.                                    \tag{2.1}
\]

The slack-one rigidity theorem says that every adjacent pair in `C_1` is a
different selected five-set witness.  Hence every interval of length at least
two in `C_1` has rank at least five.  Equivalently:

> Every target of rank at most four represented in `C_1` occurs as a literal
> entry of `C_1`.

The component capacities are

\[
 K_1=q_1+1=n_1,\qquad K_2=2q_2+3=2n_2-1.               \tag{2.2}
\]

Also

\[
q_1+q_2=462-z,qquad n_1+n_2=465-z.                    \tag{2.3}
\]

## 3. Literal localization theorem

### Theorem 3.1

For every nonempty `S subseteq [11]` with `|S|<=4`,

\[
 S\cap D_2\ne\varnothing
 \quad\Longrightarrow\quad
 \text{some position of }C_1\text{ is literally equal to }S. \tag{3.1}
\]

Consequently (1.1) holds, and

\[
 n_1\ge
 \Phi(d):=\sum_{s=1}^{4}
 \left(\binom{11}{s}-\binom{11-d}{s}\right),
 \qquad d=|D_2|.                                      \tag{3.2}
\]

#### Proof

Every rank-at-most-four witness lies wholly in one of `C_1,C_2`, since a
literal five-set position cannot belong to such a witness.  If
`S intersect D_2` is nonempty, then `S` is not contained in `V_2`, so no
interval of `C_2` can have OR `S`.  Universality therefore places a witness
for `S` in `C_1`.

By slack-one rigidity, a lower target represented in `C_1` must be a
singleton physical interval.  Thus an entry of `C_1` equals `S`.

For fixed rank `s`, exactly

\[
 \binom{11}{s}-\binom{11-d}{s}
\]

sets meet `D_2`.  Distinct literal values require distinct physical
positions, proving (1.1) and (3.2).  QED.

The conclusion is set-valued, not merely numerical: for a particular deficit
`D_2`, the complete family

\[
 \{S:1\le|S|\le4,\ S\cap D_2\ne\varnothing\}
\]

is prescribed inside `C_1`.

## 4. Exact numerical consequences

The complete lower ideal has size

\[
 L_5=\sum_{s=1}^{4}\binom{11}{s}=561.                  \tag{4.1}
\]

The component Hall inequality specializes to

\[
 \boxed{
 561\le
 \min\{n_1,L_4(|V_1|)\}
 +\min\{2n_2-1,L_4(|V_2|)\},}                         \tag{4.2}
\]

where

\[
 L_4(v)=\sum_{s=1}^{4}\binom{v}{s}.                   \tag{4.3}
\]

The separate physical-capacity part of (4.2) gives

\[
 q_2\ge95+z,qquad n_2=q_2+2\ge97+z.                  \tag{4.4}
\]

Using (2.3),

\[
 n_1\le368-2z.                                         \tag{4.5}
\]

The literal-family lower bounds are

\[
\begin{array}{c|rrrr|r}
d& a_1(C_1)&a_2(C_1)&a_3(C_1)&a_4(C_1)&\Phi(d)\\ \hline
0&0&0&0&0&0\\
1&1&10&45&120&176\\
2&2&19&81&204&306\\
3&3&27&109&260&399.
\end{array}                                             \tag{4.6}
\]

Since the two components need at least one literal five-set separator,
`z>=1`, so (4.5) gives `n_1<=366`.  The `d=3` row of (4.6) is impossible.
This proves (1.2).

Combining (3.2) and (4.5) more carefully gives

* `d=2` only if `306<=368-2z`, hence `z<=31`;
* `d=1` only if `176<=368-2z`, hence `z<=96`.

This proves (1.3).

There is a useful redundancy distinction.  Since the `q_2` selected
rank-five targets in `C_2` are distinct and contained in `V_2`, one also has

\[
 q_2\le \binom{|V_2|}{5}.                             \tag{4.6a}
\]

Together with `q_2>=95+z`, this already excludes `|V_2|<=8`, and for
`|V_2|=9` it gives `95+z<=126`, or `z<=31`.  Thus the deficit-two bound and
the first breakpoint in (1.3) are also consequences of natural rank-five
component eligibility, although the current production summaries do not
materialize that count.  The genuinely new numerical breakpoint is

\[
 |V_2|=10\quad\Longrightarrow\quad z\le96,             \tag{4.6b}
\]

along with the four rank-by-rank literal-family rows in (4.6).

When `V_1=[11]`, equation (4.2) can also be written as the useful exact
profile row

\[
 \boxed{L_4(|V_2|)\ge561-n_1=96+z+n_2.}               \tag{4.7}
\]

The three possible support sizes then have the sharp thresholds

\[
\begin{array}{c|c}
|V_2|&\text{necessary condition}\\ \hline
9&n_2+z\le159,\\
10&n_2+z\le289,\\
11&\text{automatic}.
\end{array}                                             \tag{4.8}
\]

## 5. Why the cut was absent from the earlier structural summaries

The existing Type-II circuit separately enforces:

* two component slacks `{1,2}`;
* one coordinate-complete component;
* the slack-one adjacent-pair row;
* the physical named-cell inequality equivalent to `q_2>=95+z`.

Those separate summaries, even after adding the natural rank-five support
cap `q_i<=C(|V_i|,5)`, admit the abstract profile

\[
 z=97,\quad(q_1,q_2)=(173,192),\quad(n_1,n_2)=(174,194),
 \quad(|V_1|,|V_2|)=(11,10).                           \tag{5.1}
\]

Indeed `q_2=192<=C(10,5)=252`,
`K_1+K_2=174+387=561`, and the separate coordinate-eligibility total is
`L_4(11)+L_4(10)=561+385>=561`.  But the coupled Hall total is only

\[
 \min(174,561)+\min(387,385)=559<561.                  \tag{5.2}
\]

Thus the `z>=97` completeness breakpoint is genuinely absent from the
separate component-capacity, coordinate-support, and natural rank-five
eligibility summaries.  The rank-by-rank rows are stronger still.  The
complete base OR formula logically implies every valid theorem here; the
purpose of a dedicated circuit is to expose these consequences early, not
to add a new semantic restriction to the original problem.

## 6. Exact guarded encoding

The Type-II plan already has exact flags for

* the first and second low components;
* which component is slack one;
* an existentially selected coordinate-complete component;
* every entry rank and the literal-five count `z`.

The optional guard

```text
K11_FOREST_TWO_COMPONENT_PIN_LOCALIZATION=1
```

adds the theorem without target-by-target witness variables:

1. materialize exact slack-one and slack-two component memberships;
2. materialize the eleven coordinate-OR bits of the slack-two component;
3. enforce `|D_2|<=2`, `|D_2|>=1 => z<=96`, and
   `|D_2|>=2 => z<=31`;
4. count ranks one through four inside the slack-one component and impose the
   two rows of (4.6) when `|D_2|>=1` or `>=2`.

All gates are bidirectional and all substantive rows are dormant outside the
two-component branch.  The exact incremental inventory is

```text
11,604 variables / 57,705 clauses.
```

The rank counters expose the stronger literal-family content while avoiding
561 target selectors.  A smaller reuse plan is recorded in the independent
audit, but the implemented circuit is exact and fully guarded.

## 7. Finite verification and scope

The independent checker

```text
python3 scratch/check_k11_two_component_pin_localization.py
```

verifies all arithmetic, exhausts the abstract integer profiles, reproduces
the corrected strictness example (5.1), exhausts the production gate and
comparator truth tables, recomputes the exact circuit inventory, and checks
the literal-localization implication whenever its antecedent occurs in the
archived exact words through `k=9`.
The standard archived optima have no two-low-component `{1,2}` profile, so
the solved-case check is honest but vacuous; the theorem is established by
the proof above, not by those certificates.

The theorem applies only to the Type-II two-component branch.  If the
slack-two component is coordinate-complete, the slack-one component may have
a large deficit; a long enough slack-two component can carry the missing
lower targets.  Therefore no symmetric unconditional deficit-two bound is
claimed.

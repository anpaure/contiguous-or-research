# Prospective `M0` is an oriented-diamond selection with an exact residual Hall row

Date: 2026-08-01  
Lane: Thread D / protected pivot / upper--tail--head correlation  
Status: dependency-clean exact reduction, exact fractional point, literal
Boolean non-TU obstruction, and exact graphic completion row.  No
all-dimensional existence claim is made.

## 0. Verdict

Choosing `M0` jointly with the upper representatives is strictly more
structured than applying a generic rainbow-matching theorem to a fixed
`M0`.  The joint problem has the following exact Boolean form.

For every rank-`m+1` upper set `R`, choose one **oriented diamond**

\[
             d=(R;L,T,V),\qquad T\cap V=L,\quad T\cup V=R,              \tag{0.1}
\]

where `|L|=m-1` and `|T|=|V|=m`.  The chosen diamonds must have distinct
`L`, distinct `T`, and distinct `V`.  The unused lower vertices and unused
`T` vertices must then admit a perfect incidence matching.  That last
condition is an ordinary bipartite Hall/min-cut condition and is exactly
what extends the selected pairs `L->T` to a perfect `M0`.

Thus prospective choice removes the artificial fixed-`M0` head map, but it
does not turn the problem into one network flow.  The oriented-diamond
selection has four partition resources `(R,L,T,V)`.  Its literal Boolean
constraint matrix contains a determinant-two triangle already for `m=3`,
and the same triangle embeds in every `m>=3`.  Consequently neither total
unimodularity nor an ordinary Hall theorem follows from the Boolean
incidence alone.

The tight-pivot predecessor phase fixes a compatible path of oriented
diamonds.  The small protected-matching theorem proves that its `L->T`
pairs extend to some `M0` when its length is at most `m-1`.  What remains
unproved is simultaneous completion of all upper colours while retaining
head injectivity and the residual Hall row.  A directed-linear-forest
output additionally requires the graphic inequalities on the selected
arcs `T->V`; cycle breaking is not automatic after a head/tail matching.

## 1. Boolean notation

Let the ground set have size `2m-1`, and put

\[
 \mathcal L={ [2m-1]\choose m-1},\qquad
 \mathcal O={ [2m-1]\choose m},\qquad
 \mathcal U={ [2m-1]\choose m+1}.                       \tag{1.1}
\]

Write

\[
 W=|\mathcal L|=|\mathcal O|,qquad
 U=|\mathcal U|={m-1\over m+1}W,qquad
 C=W-U={2W\over m+1}=\operatorname {Cat}_m.             \tag{1.2}
\]

An oriented diamond is equivalently specified by \(R\in\mathcal U\) and an
ordered pair of distinct elements `a,b in R`:

\[
 L=R-\{a,b\},\qquad T=R-\{b\},\qquad V=R-\{a\}.         \tag{1.3}
\]

The physical predecessor incidence is `L--T`; the successor incidence is
`L--V`; and the rooted middle-owner arc is `T->V`, of upper colour `R`.

## 2. Exact prospective-`M0` equivalence

Let \(\mathcal D\) be the set of all oriented diamonds.  For
\(d\in\mathcal D\),
write `R(d),L(d),T(d),V(d)` for its four entries.

### Theorem 2.1 (oriented diamonds plus residual Hall)

The following are equivalent.

1. There is a perfect incidence matching
   \(M_0:\mathcal L\to\mathcal O\) and an
   incidence matching `Q` outside `M0` which contains exactly one edge of
   every upper colour, with distinct rooted tails and heads.
2. There is a set \(X\subseteq\mathcal D\) such that

   * every \(R\in\mathcal U\) occurs exactly once in `X`;
   * the values `L(d)` are distinct over `d in X`;
   * the values `T(d)` are distinct over `d in X`;
   * the values `V(d)` are distinct over `d in X`; and
   * after deleting `L(X)` and `T(X)`, the residual inclusion graph

     \[
       G_X=\bigl(\mathcal L-L(X),\ \mathcal O-T(X);\ L\subset T\bigr)
                                                                    \tag{2.1}
     \]

     has a perfect matching.

For a fixed `X`, the last condition is equivalent to the exact Hall family

\[
 |\nabla A\setminus T(X)|\ge |A|
       \quad\hbox{for every }A\subseteq\mathcal L-L(X),              \tag{2.2}
\]

where
\(\nabla A=\{T\in\mathcal O:L\subset T\text{ for some }L\in A\}\).

#### Proof

Given `(M0,Q)`, let `L--V` be the unique `Q` edge of colour `R`, and put
`T=M0(L)`.  Since the colour is `T union V=R` and both middle sets contain
`L`, they are the two corners of (0.1).  The matching properties of `M0`
and `Q` give distinct `L,T,V`.  Removing these selected `L->T` pairs from
`M0` leaves a perfect matching of (2.1).

Conversely, use every selected diamond to set

\[
                       M_0(L(d))=T(d),\qquad Q(L(d))=V(d).             \tag{2.3}
\]

Extend the first assignment by a perfect matching of `G_X`.  The distinct
`L,T` rows make `M0` perfect, and distinct `L,V` make `Q` a matching.
Equation (0.1) gives upper colour `R(d)`, used exactly once.  Finally,
(2.2) is precisely Hall's theorem for `G_X`.  \(\square\)

The residual test is therefore polynomial for a *given* oriented-diamond
selection: one bipartite maximum matching or one min-cut supplies either
the extension or a literal deficient set `A`.  The theorem does not say
that a suitable `X` always exists.

### Corollary 2.2 (exact binary model)

Introduce binary variables `x_d` for diamonds and `y_(L,T)` for inclusion
pairs `L subset T`.  Prospective head/tail/upper feasibility is exactly

\[
\begin{aligned}
 \sum_{d:R(d)=R}x_d&=1                         &&(R\in\mathcal U),\\
 \sum_{d:L(d)=L}x_d+\sum_{T\supset L}y_{L,T}&=1&&(L\in\mathcal L),\\
 \sum_{d:T(d)=T}x_d+\sum_{L\subset T}y_{L,T}&=1&&(T\in\mathcal O),\\
 \sum_{d:V(d)=V}x_d&\le1                     &&(V\in\mathcal O),\\
 x_d,y_{L,T}&\in\{0,1\}.                                             \tag{2.4}
\end{aligned}
\]

The `y` variables are exactly the residual part of `M0`; they are not an
independent compiler or topology choice.

## 3. Protected tight-pivot phase

Let

\[
 V_0,V_1,\ldots,V_\ell                                             \tag{3.1}
\]

be the protected simple Johnson path and put

\[
 L_i=V_i\cap V_{i+1},\qquad R_i=V_i\cup V_{i+1}.                     \tag{3.2}
\]

The correlated predecessor/successor phase fixes the oriented diamonds

\[
                 d_i=(R_i;L_i,V_i,V_{i+1})\qquad(0\le i<\ell).       \tag{3.3}
\]

Their `L,T,V,R` entries are injective in the required directions and their
rooted arcs form the directed path

\[
                         V_0\to V_1\to\cdots\to V_\ell.              \tag{3.4}
\]

When `ell<=m-1`, the protected small-matching extension theorem proves that
the partial predecessor matching `L_i->V_i` extends to at least one perfect
`M0`.  Equivalently, if no other diamonds have yet been selected, its
residual Hall row (2.2) holds.

This is exactly the safe conclusion.  After the remaining `U-ell`
diamonds are selected, their consumed `L` and `T` vertices change (2.2), so
the small-extension theorem cannot be invoked a second time without
checking the new residual graph.  The desired protected theorem is thus a
binary solution of (2.4) with `x_(d_i)=1`, not a fixed-`M0` generic rainbow
claim.

## 4. Fractional feasibility is automatic even prospectively

Every upper `R` supports `m(m+1)` oriented diamonds.  Every fixed lower
`L`, tail corner `T`, or head corner `V` occurs in exactly `m(m-1)` of
them.  Hence

\[
             x_d={1\over m(m+1)},\qquad
             y_{L,T}={2\over m(m+1)}\quad(L\subset T)                 \tag{4.1}
\]

satisfies the linear relaxation of (2.4): each upper row has load one;
each `L` and `T` row has load

\[
                     {m-1\over m+1}+{2\over m+1}=1;                  \tag{4.2}
\]

and each head row has load `(m-1)/(m+1)<1`.

Thus prospective choice removes no fractional obstruction.  The remaining
issue is integral correlation among the four diamond resources and the
residual matching.

## 5. A literal Boolean determinant-two minor

The integral matrix in (2.4) is not totally unimodular.  For `m=3`, use
the following three genuine oriented diamonds on `[5]`:

\[
\begin{array}{c|c|c|c}
R&L&T&V\\ \hline
1234&34&234&134\\
1234&24&124&234\\
2345&34&345&234.
\end{array}                                                           \tag{5.1}
\]

Restrict the constraint matrix to the three rows

\[
              R=1234,\qquad L=34,\qquad V=234.                       \tag{5.2}
\]

and the three columns in (5.1).  The resulting matrix is

\[
                   \begin{pmatrix}
                    1&1&0\\
                    1&0&1\\
                    0&1&1
                   \end{pmatrix},
              \qquad\det=-2.                                        \tag{5.3}
\]

For every `m>3`, adjoining one fixed `(m-3)`-set to every entry of (5.1)
embeds the same minor in the rank-`m` system.  Therefore a proof based on
total unimodularity, a directed-network matrix, or ordinary bipartite Hall
cannot be valid without an additional structural restriction.

The obstruction is dimension-minimal: at `m=2` there is only one upper
colour, so no three-column correlation is possible.

This is a matrix obstruction, not an infeasible full Boolean instance.  It
isolates the smallest unavoidable local integral correlation but does not
disprove existence of a global jointly chosen `(M0,Q)`.

## 6. Relation to generic rainbow matching

For a fixed `M0`, the rooted-arc system is an edge-coloured bipartite graph
with upper colour-class size \(m+1\) and maximum endpoint degree
\(\Delta=m-1\).
Generic full-rainbow results for graphs require colour classes larger than
`2` times the maximum degree; that hypothesis already fails at `m=3`
and is decisively false
in the intended range `m>=4`:

\[
                         m+1\not>2(m-1).                              \tag{6.1}
\]

At `m=4`, the Boolean numbers are exactly (m+1=2\Delta-1), the sharp
scale of Wdowinski's abstract no-full-rainbow constructions; for larger
`m` the ratio is still worse.  Hence neither the
Aharoni--Berger--Meshulam
criterion nor a fictitious (|\text{colour}|>\Delta) shortcut applies.  A positive
result must use the oriented-diamond/residual-incidence structure or an
equally strong correlation with `M0`.

The fixed-`M0` tensor nevertheless has exact strict *marginal* slack: for
every upper-colour family `S`, the union graph has matching number at least

\[
             \left\lceil {m+1\over m-1}|S|\right\rceil>|S|.          \tag{6.2}
\]

Thus ordinary union-Hall cuts are not the missing condition.  The failure
is precisely the simultaneous colour/tail/head choice.

## 7. The graphic row and cycle breaking

Under Theorem 2.1, root every selected successor incidence as the arc

\[
                              T(d)\longrightarrow V(d).              \tag{7.1}
\]

Distinct `T` and `V` make these arcs a directed partial permutation.  It is
a directed linear forest exactly when one adds the graphic inequalities

\[
 \sum_{d:\ T(d),V(d)\in S}x_d\le |S|-1
       \qquad(\varnothing\ne S\subseteq\mathcal O).                  \tag{7.2}
\]

Consequently (2.4), (7.2), and the protected equations `x_(d_i)=1` are a
dependency-clean exact model of the decisive owner gate.

If (7.2) holds, the `U` selected arcs on `W` rooted vertices have exactly

\[
                              W-U=\operatorname {Cat}_m              \tag{7.3}
\]

path components.  If a head/tail matching has `z` directed cycle
components instead, it has `Cat_m+z` total components and no free port on
those `z` cycles.  There is no general colour-preserving cycle-breaking
theorem: replacing representatives must preserve colour, tail, head, and
graphic independence simultaneously.  Relative to a chosen rainbow
matching, the exact exchange test is common independence in the four
contracted colour/tail/head/graphic matroids, as recorded in
`MATH_THEOREM_THREAD_D_RAINBOW_MATCHING_CYCLE_BREAKING_AND_ROOTED_FOREST_GATE_20260801.md`.

Thus cycles should either be forbidden prospectively by (7.2), or broken
by a proved balanced packet.  They cannot be deferred to the later
one-defect component connector Hall theorem.

## 8. Finite audit and exact surviving theorem

For the displayed `m=3` Boolean `M0` used in the rooted-arc audit, exact
enumeration finds 329 colour-saturating tail/head matchings.  Every simple
correlated predecessor path with distinct upper colours extends at this
matching level: respectively `20/20,20/20,20/20,20/20,5/5` paths of
length `1,2,3,4,5`.  In particular, the previously isolated path

\[
                         A\to D\to J\to F\to C                        \tag{8.1}
\]

has three head/tail/upper completions.  Its obstruction is downstream
Hamilton-path completion, not three-partite matching.  This is positive
finite evidence
only; it is not an all-`m` theorem and the actual tight pivot begins in a
larger parameter range.

The exact theorem still required for the pivot-rich packet is now:

> For every admissible tight-pivot protected bank (3.3), the system
> (2.4), (7.2), and `x_(d_i)=1` has an integral solution.

Dropping (7.2) asks only for the jointly chosen upper/tail/head matching;
adding it asks for the protected upper-surjective directed linear forest.
Fractional feasibility, ordinary marginal Hall, and initial extension of
the pivot predecessor phase are all proved.  The determinant-two minor
(5.3) shows why those facts do not round automatically.  No Boolean full
instance with unavoidable integral deficiency is exhibited here, and no
all-dimensional existence claim is made.

## 9. Audit artifacts used

The fixed-`M0` degree and fractional ledger is independently recorded in

`MATH_THEOREM_THREAD_D_FIXED_M0_ROOTED_ARC_RAINBOW_HYPERGRAPH_GATE_20260801.md`.

The exact `m=3` extension census is replayed by

* `scratch/audit_threadD_m3_correlated_path_colour_bimatching_20260801.py`;
* `scratch/threadD_m3_correlated_path_colour_bimatching_20260801.audit.json`.

The present prospective reduction is symbolic; no finite-search result is
used in Theorem 2.1 or Section 7.

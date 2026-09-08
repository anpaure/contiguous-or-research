# Row-target capacity: exact Hall and localized collision identities

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

For a variable exact wreath factor, the physically weakest row-specific
phase selection is a capacitated bipartite matching, not a packing which
must either fill or discard an entire seed row.  Its defect has two exact
forms:

\[
 \boxed{
 \ell_q(F)=\max_{A\subseteq F}
 \bigl(\kappa_q|A|-|N_q(A)|\bigr)_+}
 \tag{0.1}
\]

and

\[
 \boxed{
 \ell_q(F)=\max_{A\subseteq F}
 \left[
  \sum_S(\mu_{A,q}(S)-1)_+
  -(n-\kappa_q)|A|
 \right]_+.}
 \tag{0.2}
\]

Here

\[
 \kappa_q=\left\lfloor\frac{N_q}{T}\right\rfloor,
 \qquad
 \delta_q=N_q-\kappa_qT,
\]

and \(\mu_{A,q}\) is the depth-\(q\) multiplicity contributed by the
subfamily \(A\) of wreath rows.  The exact number of uncertified targets
is

\[
 \boxed{N_q-\nu_q(F)=\delta_q+\ell_q(F).}
 \tag{0.3}
\]

Thus the sharp row-specific floor ledger is

\[
 \sum_{q,\pm}\ell_q^\pm=o(W),
\]

in addition to the already automatic floor term
\(\sum_{q,\pm}\delta_q=o(W)\).  This strictly weakens a full-star leave
ledger \(\sum\kappa_qL_q=o(W)\).

The global MWB overload and the global factorial excess do not imply
(0.1) as abstract incidence-graph statements: they see only the final
right-degree histogram, whereas (0.1) is hereditary over every row
subfamily.  Conversely, zero Hall slot defect does not imply small MWB
overload.  A wreath-specific implication would require a new hereditary
cyclic expansion theorem.

## 1. Setup

Put

\[
 n=2m+1,\qquad W=\binom nm,\qquad T=W/n,
 \qquad N_q=\binom n{m-q}.
\]

Let \(F=\{\pi_1,\ldots,\pi_T\}\) be an exact middle wreath factor.  For
one lower row \(q\), form the bipartite graph \(G_q(F)\) with left class
\(F\), right class \(\binom{[n]}{m-q}\), and

\[
 \pi_iS\in E(G_q(F))
 \quad\Longleftrightarrow\quad
 S=I_{\pi_i}(j,m-q)\text{ for some }j\in\mathbb Z_n.
\]

Every left degree is exactly \(n\).  For \(A\subseteq F\), write

\[
 N_q(A)=\bigcup_{\pi\in A}N_q(\pi)
\]

and

\[
 \mu_{A,q}(S)=\#\{\pi\in A:S\in N_q(\pi)\}.
 \tag{1.1}
\]

Then

\[
 \sum_S\mu_{A,q}(S)=n|A|.
 \tag{1.2}
\]

The upper complementary row is identical after reversing/complementing
the cyclic orders, so all statements below apply separately to both signs.

## 2. Exact capacitated Hall theorem

Give every left row capacity \(\kappa_q\) and every right target capacity
one.  Let \(\nu_q(F)\) be the maximum number of selected incidences and
define

\[
 \ell_q(F)=\kappa_qT-\nu_q(F).
 \tag{2.1}
\]

### Theorem 2.1

Equations (0.1) and (0.3) hold.

#### Proof

Replace every left row by \(\kappa_q\) identical clones.  Ordinary
bipartite matching in the clone graph is exactly the capacitated matching
above.  The Hall-deficiency theorem says that the number of unmatched
left clones is

\[
 \max_X(|X|-|N(X)|)_+.
\]

For a fixed support \(A\subseteq F\), this expression is maximized by
taking all \(\kappa_q\) clones of every row of \(A\), because adding a
clone changes no neighborhood and increases \(|X|\).  Thus the maximum is
exactly (0.1).

Finally,

\[
 N_q-\nu_q(F)
 =N_q-(\kappa_qT-\ell_q(F))
 =\delta_q+\ell_q(F),
\]

which proves (0.3). \(\square\)

### Corollary 2.2 (full-star packing)

Let \(L_q^{\rm star}\) be the minimum number of rows discarded so that
every retained row can be assigned \(\kappa_q\) distinct targets and no
target is assigned twice.  Then

\[
 \boxed{
 \left\lceil\frac{\ell_q(F)}{\kappa_q}\right\rceil
 \le L_q^{\rm star}\le\ell_q(F).}
 \tag{2.2}
\]

Indeed, a full-star packing leaving \(L\) rows gives a capacitated matching
of size \(\kappa_q(T-L)\), so \(\ell_q\le\kappa_qL\).  Conversely, in a
maximum capacitated matching the sum of the unsupplied capacities is
\(\ell_q\); therefore at most \(\ell_q\) rows are partially supplied.
Discard those rows and retain the full stars on all other rows.

For \(\kappa_q\ge2\), the full-star problem is a genuine hypergraph
matching problem and has no ordinary Hall min--max formula in general.
The capacitated slot formulation is both weaker and exactly solvable.

## 3. Exact localized collision identity

For an integer \(d\ge0\),

\[
 d-\mathbf1_{d>0}=(d-1)_+.
\]

Using (1.2),

\[
 |N_q(A)|
 =n|A|-\sum_S(\mu_{A,q}(S)-1)_+.
 \tag{3.1}
\]

Substituting (3.1) into (0.1) proves (0.2).

This has an exact factorial expansion.  Put

\[
 F_{A,q,r}=\sum_S\binom{\mu_{A,q}(S)}r.
\]

The scalar identity

\[
 (d-1)_+=\sum_{r=2}^d(-1)^r\binom dr
\]

gives

\[
 \boxed{
 \ell_q(F)=\max_{A\subseteq F}
 \left[
  \sum_{r\ge2}(-1)^rF_{A,q,r}
  -(n-\kappa_q)|A|
 \right]_+.}
 \tag{3.2}
\]

In particular, since \((d-1)_+\le\binom d2\),

\[
 \boxed{
 \ell_q(F)\le
 \max_{A\subseteq F}
 \left[
  \sum_S\binom{\mu_{A,q}(S)}2
  -(n-\kappa_q)|A|
 \right]_+.}
 \tag{3.3}
\]

The pair moment in (3.3) is also

\[
 \sum_{\{\pi,\pi'\}\subseteq A}
 |N_q(\pi)\cap N_q(\pi')|.
\]

Thus the relevant collision theorem is hereditary and baseline-corrected:
it must control every row subfamily after subtracting
\((n-\kappa_q)|A|\).  A global collision moment at \(A=F\) is not enough.

## 4. Complement form and actual support holes

Let

\[
 h_q(F)=N_q-|N_q(F)|
\]

be the actual row-support holes.  For \(B\subseteq F\), let

\[
 g_q(B)=|N_q(F)\setminus N_q(F\setminus B)|
\]

be the number of supported targets all of whose incident rows lie in
\(B\).  Writing \(A=F\setminus B\) in (0.1) gives

\[
 \boxed{
 \ell_q(F)=\max_{B\subseteq F}
 \bigl(h_q(F)-\delta_q+g_q(B)-\kappa_q|B|\bigr)_+.}
 \tag{4.1}
\]

Taking \(A=F\) in (0.1) yields

\[
 \ell_q(F)\ge(h_q(F)-\delta_q)_+,
\]

and therefore

\[
 \boxed{h_q(F)\le\delta_q+\ell_q(F).}
 \tag{4.2}
\]

The inequality may be strict: the per-row cap can create an artificial
selection defect even when every target is already present in the emitted
cyclic blocks.

## 5. Relation to MWB and factorial excess

MWB uses a different floor parameter,

\[
 b_q=\left\lfloor\frac{W}{N_q}\right\rfloor,
\]

and measures the distance of the final right-degree histogram
\(\mu_{F,q}=\mu_{F,q}(F)\) from the balanced values
\(b_q,b_q+1\).  The Hall defect \(\ell_q\), by contrast, depends on
\(\mu_{A,q}\) for every \(A\subseteq F\).

There is therefore no black-box implication in either direction.

### Example 5.1 (zero overload and zero factorial excess, positive Hall defect)

Take the depth-one numerical parameters \(n=7,T=5,N=21\), so
\(\kappa=4,\delta=1\), and make an abstract left-7-regular bipartite
graph with neighborhoods

\[
 N(1)=N(2)=\{1,\ldots,7\},
\]

\[
 N(3)=N(4)=\{8,\ldots,14\},
\]

\[
 N(5)=\{15,\ldots,21\}.
\]

The right-degree histogram is exactly \(2^{14}1^7\), the balanced
histogram for total mass \(35\) on \(21\) targets.  Hence the MWB overload
and every balanced factorial excess vanish.  But the family
\(A=\{1,2,3,4\}\) has

\[
 \kappa|A|-|N(A)|=16-14=2,
\]

so \(\ell=2\).

This is an abstract incidence example, not an exact wreath factor.  It
proves that a theorem using only the global multiplicity histogram cannot
establish hereditary Hall expansion; cyclic geometry would have to supply
the missing input.

### Example 5.2 (zero Hall slot defect, large overload)

On the same parameters, assign four distinct private targets to each of
five rows, using targets \(1,\ldots,20\).  Let
\(C=\{1,5,9,13\}\).  For rows one through four, add the three elements of
\(C\) other than that row's private element of \(C\); for row five add
\(1,5,9\).  Every row now has degree seven.

The private assignments give a capacitated matching of size \(20=\kappa
T\), so \(\ell=0\).  Target 21 is a hole, while the four common targets
have degrees \(5,5,5,4\) and the other sixteen supported targets have
degree one.  The balanced-overload value is 11.  Thus Hall feasibility
does not imply MWB.

## 6. Coefficient-one consequence

For the floor-calibrated band through \(Q\), the arithmetic term obeys

\[
 \sum_{q\le Q,\pm}\delta_q=o(W)
\]

at \(Q=\lceil\sqrt{m\log m}\rceil\).  Therefore row-specific capacitated
selection supplies the literal coefficient-one ledger as soon as

\[
 \boxed{
 \sum_{q\le Q,\pm}\ell_q^\pm(F_m)=o(W).}
 \tag{6.1}
\]

By (4.2), this implies the weak missing-shadow condition.  It is neither a
consequence of MWB nor a consequence of the global balanced factorial
excess without an additional hereditary cyclic-expansion theorem.

The exact new gate can be stated as follows:

> Construct one globally traded exact wreath factor for which every
> signed row has small baseline-corrected hereditary duplicate excess in
> the sense of (0.2), with total maximum defect (6.1).

This target is weaker than a common all-depth augmented-edge matching and
more precise than a scalar missing-shadow or collision-energy target.

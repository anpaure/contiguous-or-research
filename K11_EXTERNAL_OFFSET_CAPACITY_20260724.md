# External-offset capacity at the zero-margin \(k=11\) templates

## 1. Outcome

This note continues from the audited conclusions of
K11_ZERO_MARGIN_WINDOW_ATTACK_20260724.md and
K11_MIDDLE_LEVELS_NEWLINE_20260724.md.

No contradiction is obtained.  The external rank-five/rank-six matching
edges do, however, satisfy an exact bounded-capacity theorem which was not
previously recorded.

Let

\[
 A_0,A_1,\ldots,A_{m-1}
\]

be the central low-entry segment, let \(H\) be its exceptional triple, and
let

\[
 E:=465-m
\tag{1.1}
\]

be the number of external matching edges.  Endpoint saturation canonically
anchors those \(E\) edges at the \(E\) physical positions outside the
central segment.  If the edge anchored at \(p\) has rank-five source
\(S_p\), rank-six target \(U_p\), and extension label

\[
 \xi_p=U_p\setminus S_p,
\]

then:

1. the anchor entry is contained in \(S_p\), and hence omits \(\xi_p\);
2. \(\xi_p\) occurs in the one-sided added cell block, at directed distance
   at most three from \(p\); and
3. for every coordinate set \(X\subseteq[11]\), the number of external
   labels lying in \(X\) is bounded simultaneously by a source Hall
   capacity, an anchor Hall capacity, and a directed offset-exposure
   capacity.

The precise result is Theorem 1 below.  If

\[
 e^{\rm ext}(X):=\#\{p:\xi_p\in X\},
\]

then

\[
\boxed{
 e^{\rm ext}(X)
 \le
 \min\{E-s_X,\ E-a_X,\ d_X\}
 \le 3u_X.
}
\tag{1.2}
\]

Here \(s_X\) is the number of external rank-five sources containing \(X\),
\(a_X\) is the number of external anchor entries containing \(X\), \(d_X\)
is the exact directed exposure count, and \(u_X\) is the number of
outer-or-boundary-halo positions whose entry meets \(X\).

The full matching-extension hierarchy also enters exactly.  If
\(\kappa_X^{\rm cen}\) is the number of central matching edges which
complete \(X\), and \(1\le |X|=t\le6\), then

\[
\boxed{
 \Delta_t-\kappa_X^{\rm cen}
 \le e^{\rm ext}(X),
 \qquad
 \Delta_t=\binom{11-t}{6-t}-\binom{11-t}{5-t}.
}
\tag{1.3}
\]

Thus every completion not supplied by the central block must be carried by
one of the physically exposed external labels in \(X\).

For a singleton \(X=\{x\}\), all of this collapses to one exact new
zero-run capacity.  If the zero runs of \(x\) in the central incidence word
have lengths \(\ell\), put

\[
 K_x:=\sum_{\ell}(\ell-3)_+.
\tag{1.4}
\]

Then

\[
\boxed{K_x\le210\qquad(x\in[11]).}
\tag{1.5}
\]

Equivalently, every coordinate has at most \(210\) all-zero four-windows in
the central segment.  The source-capacity proof of (1.5) uses exactly

\[
 e_x^{\rm ext}=43-R_x^{(3)}-\mathbf1_{x\in H}.
\]

For the \(n_5=133\) slice, (1.2) also couples the formerly separate literal
rank-five incidence, literal rank-four incidence, repeated lower-entry
incidence, and short-zero-run vectors; see Theorem 3.

There is an important negative conclusion.  In every classified
zero-margin slice one has \(E\ge132\), whereas the number of six-sets
containing a fixed pair is only \(126\).  Therefore the coarse
layer-capacity consequence of the complete subset-extension hierarchy is
nontrivial only for single coordinates.  Any contradiction must use the
actual set-valued Hall or directed-exposure inequalities in (1.2), not
merely their rankwise sums.

All arguments are finite and deterministic.  No search, solver, or
enumeration is used.

## 2. The external anchor bijection

Use physical positions \(0,1,\ldots,464\), and let the central segment
occupy

\[
 [L,R],\qquad m=R-L+1.
\tag{2.1}
\]

Fix the selected rank-five and rank-six witness families and index them in
increasing endpoint order.  Relative to these fixed witnesses, the audited
endpoint-saturation theorem says:

* every \(p<L\) is the common left endpoint of exactly one external
  rank-five/rank-six matched pair;
* every \(p>R\) is the common right endpoint of exactly one such pair;
* the rank-five interval is physically contained in the rank-six interval;
  and
* every selected interval has at most four physical cells.

Thus the external matching edges are canonically indexed by

\[
 \mathcal P_{\rm ext}:=[0,L-1]\cup[R+1,464],
 \qquad |\mathcal P_{\rm ext}|=E.
\tag{2.2}
\]

For \(p\in\mathcal P_{\rm ext}\), write

\[
 I_p\subsetneq J_p,
 \qquad
 S_p=\operatorname{OR}(I_p),
 \qquad
 U_p=\operatorname{OR}(J_p),
\tag{2.3}
\]

for the matched rank-five and rank-six witnesses and their target values.
Then

\[
 |S_p|=5,\qquad |U_p|=6,\qquad
 \xi_p:=U_p\setminus S_p
\tag{2.4}
\]

is a singleton coordinate.

Let \(B_p\) be the literal word entry at the anchor position \(p\).  Since
\(p\in I_p\),

\[
 B_p\subseteq S_p.
\tag{2.5}
\]

In particular,

\[
 \xi_p\notin B_p.
\tag{2.6}
\]

Let

\[
 D_p:=J_p\setminus I_p
\tag{2.7}
\]

be the added physical cell block.  It is nonempty.  If \(p<L\), it lies to
the right of \(I_p\); if \(p>R\), it lies to the left.  Since \(J_p\) has at
most four cells, every position in \(D_p\) has directed distance at most
three from \(p\).  Finally,

\[
 \xi_p\in\operatorname{OR}(D_p),
\tag{2.8}
\]

because \(S_p\cup\operatorname{OR}(D_p)=U_p=S_p\sqcup\{\xi_p\}\).

Equations (2.5), (2.6), and (2.8) are the physical content of the external
offset schedule needed below.

## 3. The set-valued capacity theorem

For \(X\subseteq[11]\), define

\[
\begin{aligned}
 e^{\rm ext}(X)
   &:=\#\{p\in\mathcal P_{\rm ext}:\xi_p\in X\},\\
 s_X
   &:=\#\{p\in\mathcal P_{\rm ext}:X\subseteq S_p\},\\
 a_X
   &:=\#\{p\in\mathcal P_{\rm ext}:X\subseteq B_p\},\\
 d_X
   &:=\#\{p\in\mathcal P_{\rm ext}:
       \operatorname{OR}(D_p)\cap X\ne\varnothing\}.
\end{aligned}
\tag{3.1}
\]

Define the outer boundary halo

\[
 \mathcal H_{\rm ext}
 :=[0,L+2]\cup[R-2,464],
\tag{3.2}
\]

and put

\[
 u_X:=\#\{t\in\mathcal H_{\rm ext}:B_t\cap X\ne\varnothing\}.
\tag{3.3}
\]

The classified central segments have length much larger than six, so the
two intervals in (3.2) are disjoint.

### Theorem 1 — external Hall and offset capacity

For every \(X\subseteq[11]\),

\[
\boxed{
 e^{\rm ext}(X)
 \le
 \min\{E-s_X,\ E-a_X,\ d_X\}
 \le3u_X.
}
\tag{3.4}
\]

Let \(X\ne\varnothing\) have size \(t\le6\).  For a generic matching edge
\(S\subset U\), say that it completes \(X\) when

\[
 X\subseteq U,\qquad X\nsubseteq S.
\]

Let \(\kappa_X^{\rm cen}\) and \(\kappa_X^{\rm ext}\) be the numbers of
central and external matching edges which complete \(X\).

Then

\[
\boxed{
 \kappa_X^{\rm ext}
 =\Delta_t-\kappa_X^{\rm cen}
 \le e^{\rm ext}(X),
}
\tag{3.5}
\]

where

\[
 \Delta_t
 =\binom{11-t}{6-t}-\binom{11-t}{5-t}.
\tag{3.6}
\]

### Proof

If \(\xi_p\in X\), then \(X\nsubseteq S_p\), because
\(\xi_p\notin S_p\).  Hence at most the \(E-s_X\) sources not containing
\(X\) can carry a label in \(X\).

Similarly, (2.6) shows that \(X\nsubseteq B_p\), so at most \(E-a_X\)
anchors can carry a label in \(X\).  Equation (2.8) shows that every such
anchor is counted by \(d_X\).  This proves the first inequality in (3.4).

For every anchor counted by \(d_X\), select one position
\(t\in D_p\) whose entry meets \(X\).  A prefix position \(t\) can be
reached only from \(p=t-1,t-2,t-3\), and the same assertion with reversed
orientation holds in the suffix.  All possible \(t\)'s lie in
\(\mathcal H_{\rm ext}\).  Hence every position counted by \(u_X\) receives
at most three charges.  Therefore \(d_X\le3u_X\).

The complete matching-extension hierarchy says that exactly \(\Delta_t\)
matching edges complete \(X\).  Splitting them into the central and
external edges gives the equality in (3.5).  If an edge completes \(X\),
its unique extension label belongs to \(X\).  Thus every external
completion is counted by \(e^{\rm ext}(X)\), proving the remaining
inequality.  ∎

### 3.1 Exact Hall interpretation

If only the prescribed label multiplicities and the condition
\(\xi_p\notin S_p\) are retained, the inequalities

\[
 e^{\rm ext}(X)\le E-s_X
 \qquad(X\subseteq[11])
\tag{3.7}
\]

are precisely the Hall inequalities for assigning the coordinate labels to
the \(E\) external sources.  Here

\[
 \sum_xe_x^{\rm ext}=E.
\]

Indeed, make \(e_x^{\rm ext}\) copies of each
coordinate \(x\), and join a copy of \(x\) to source \(S_p\) exactly when
\(x\notin S_p\).  A family of coordinate copies with underlying support
\(X\) has neighborhood all sources which fail to contain \(X\), of size
\(E-s_X\).  Hall's theorem gives (3.7), and conversely (3.7) for every
\(X\) gives such an assignment.

Thus (3.7) is not merely a convenient pointwise estimate: it is the exact
abstract capacity obstruction before the directed physical offsets and
the distinct-six-set condition are restored.

## 4. Coupling to the full subset-extension hierarchy

Let \(c_X\) be the number of central rank-five sources containing \(X\).
If \(|X|=t\le6\), then the complete rank-five layer has

\[
 v_t=\binom{11-t}{5-t}
\tag{4.1}
\]

members containing \(X\).  Hence

\[
 s_X=v_t-c_X.
\tag{4.2}
\]

Here and below an out-of-range binomial is zero; thus (4.1)--(4.2) also
cover \(t=6\), when both sides vanish.

Substituting (4.2) in Theorem 1 gives

\[
\boxed{
 \Delta_t-\kappa_X^{\rm cen}
 \le e^{\rm ext}(X)
 \le E-v_t+c_X.
}
\tag{4.3}
\]

There is an equivalent upper-layer form.  Put

\[
 u_t=\binom{11-t}{6-t}=v_t+\Delta_t.
\tag{4.4}
\]

On a central matching edge, the upper six-set contains \(X\) either because
the source already contains \(X\), or because the edge completes \(X\).
These alternatives are disjoint.  Thus the number \(w_X^{\rm cen}\) of
central upper six-sets containing \(X\) is

\[
 w_X^{\rm cen}=c_X+\kappa_X^{\rm cen}.
\tag{4.5}
\]

The outer inequalities imply

\[
\boxed{w_X^{\rm cen}\ge u_t-E.}
\tag{4.6}
\]

This also follows directly because at most \(E\) of the \(u_t\) six-sets
containing \(X\) can belong to the external upper family.

The numerical values are

\[
\begin{array}{c|rrrrrr}
t&1&2&3&4&5&6\\ \hline
u_t&252&126&56&21&6&1\\
\Delta_t&42&42&28&14&5&1.
\end{array}
\tag{4.7}
\]

In all five \(n_5=132\) modes and in the \(n_5=133\) slice,

\[
 E\ge132.
\tag{4.8}
\]

Consequently (4.6) is nontrivial only for \(t=1\).  For every
\(t\ge2\), one has \(u_t-E\le0\).  The higher subset hierarchy can still
constrain a survivor through the actual Hall quantities \(s_X,a_X,d_X\),
but its coarse layer-size projection has no remaining force.

This explains why summing the pair, triple, or rank-four completion laws
cannot close the external gate: the external word is already longer than
every fixed-\(X\) upper star from rank two onward.

There is a second exact way to see the same loss.  Sum (3.5) over all
\(t\)-sets \(X\).  One external matching edge completes exactly
\(\binom5{t-1}\) such sets, while its singleton label lies in exactly
\(\binom{10}{t-1}\) \(t\)-sets.  Therefore

\[
 \sum_{|X|=t}\kappa_X^{\rm ext}
 =\binom5{t-1}E,
 \qquad
 \sum_{|X|=t}e^{\rm ext}(X)
 =\binom{10}{t-1}E.
\tag{4.9}
\]

The completion-to-label-capacity ratios for \(t=1,\ldots,6\) are

\[
 1,\quad\frac12,\quad\frac29,\quad\frac1{12},
 \quad\frac1{42},\quad\frac1{252}.
\tag{4.10}
\]

Thus singleton completion exactly saturates the aggregated label capacity,
whereas every higher member of the hierarchy has a built-in positive
aggregate slack.  Any use of \(t\ge2\) must again be genuinely
set-specific.

## 5. The singleton theorem and the \(210\)-tail bound

Fix a coordinate \(x\).  Let the zero runs of \(x\) in the incidence word
of \(A_0,\ldots,A_{m-1}\) have lengths \(\ell\).  Define

\[
 R_x^{(3)}:=\#\{\ell:\ell\ge3\},
\tag{5.1}
\]

\[
 J_x:=\sum_{\ell}(\ell-2)_+,
 \qquad
 K_x:=\sum_{\ell}(\ell-3)_+.
\tag{5.2}
\]

Thus \(J_x\) and \(K_x\) are respectively the numbers of all-zero triple
and four-windows for \(x\), and

\[
 J_x-K_x=R_x^{(3)}.
\tag{5.3}
\]

Write

\[
 h_x:=\mathbf1_{x\in H}.
\tag{5.4}
\]

The central selected rank-five sources are all triple windows except
\(H\).  Hence the number containing \(x\) is

\[
 c_x=m-2-J_x-h_x.
\tag{5.5}
\]

The central rank-six upper sets are all four-windows, so their number
containing \(x\) is

\[
 w_x^{\rm cen}=m-3-K_x.
\tag{5.6}
\]

Finally, the audited central/external extension law is

\[
 e_x^{\rm ext}=43-R_x^{(3)}-h_x.
\tag{5.7}
\]

### Theorem 2 — exact singleton external capacity

For every coordinate \(x\),

\[
\boxed{K_x\le210.}
\tag{5.8}
\]

Moreover,

\[
\boxed{
 43-R_x^{(3)}-h_x
 \le E-a_x,
}
\tag{5.9}
\]

and

\[
\boxed{
 43-R_x^{(3)}-h_x
 \le d_{\{x\}}
 \le3u_{\{x\}}.
}
\tag{5.10}
\]

### Proof

There are \(210\) five-sets containing \(x\).  By (5.5), the external
source family contains

\[
 s_x=210-(m-2-J_x-h_x)
\tag{5.11}
\]

such sets.  The singleton source Hall inequality in Theorem 1 gives

\[
 43-R_x^{(3)}-h_x
 \le E-s_x.
\]

Using \(E=465-m\), the right side is

\[
 E-s_x=253-J_x-h_x.
\]

After cancelling \(h_x\), this becomes

\[
 J_x-R_x^{(3)}\le210.
\]

Equation (5.3) proves (5.8).  Equations (5.9) and (5.10) are the anchor and
directed-exposure parts of Theorem 1 after substituting (5.7).  ∎

There is a second audit of (5.8).  The full rank-six layer has point degree
\(252\), while at most \(E\) external upper sets can contain \(x\).  Thus

\[
 m-3-K_x=w_x^{\rm cen}\ge252-E=m-213,
\]

which is again \(K_x\le210\).  Hence the source-label proof and the upper
layer proof close to the same exact inequality; neither has hidden slack.

More explicitly, the external point degrees themselves are

\[
 s_x^{\rm ext}=212-m+J_x+h_x,
 \qquad
 w_x^{\rm ext}=255-m+K_x,
\tag{5.12}
\]

and

\[
 w_x^{\rm ext}-s_x^{\rm ext}
 =43-R_x^{(3)}-h_x=e_x^{\rm ext}.
\tag{5.13}
\]

Thus the central zero-run statistics determine both external point-degree
vectors, not only their difference.  The inequality \(K_x\le210\) is
exactly the capacity condition \(w_x^{\rm ext}\le E\).

Summing over all coordinates gives another consistency check:

\[
 \sum_x K_x=5(m-3),
\tag{5.14}
\]

because every central four-window is a six-set and therefore omits exactly
five coordinates.  Consequently

\[
 \sum_x w_x^{\rm ext}=6E,
\]

as required for a family of \(E\) six-sets.  The pointwise bound (5.8) is
therefore not strengthened by summation; its possible force is in the
distribution of the long zero tails among the eleven coordinates.

## 6. The \(n_5=133\) rank-four bridge

Specialize now to \(n_5=133\).  Then

\[
 m=332-n_4,
 \qquad
 E=133+n_4.
\tag{6.1}
\]

Every external position contains either one of the \(133\) distinct literal
rank-five entries or one of the \(n_4\) distinct literal rank-four entries.
For a coordinate \(x\), let

* \(\ell_x^{(5)}\) be the number of literal rank-five entries containing
  \(x\);
* \(\lambda_x\) be the number of literal rank-four entries containing
  \(x\);
* \(\varrho_x\) be the incidence of \(x\) among the repeated lower entries
  of the central segment;
* \(E_{1,x},E_{2,x}\) be the numbers of zero runs of \(x\) of lengths one
  and two;
* \(i_x=\mathbf1_{x\in B_s\cap B_{s+1}}\); and
* \(b_x\) be the number of the first three and last three central positions
  whose entry contains \(x\).

The external anchor incidence is exactly

\[
 a_x=\ell_x^{(5)}+\lambda_x,
\tag{6.2}
\]

and the halo occurrence count is

\[
 u_{\{x\}}=\ell_x^{(5)}+\lambda_x+b_x.
\tag{6.3}
\]

The audited rank-four/extension bridge is

\[
 e_x^{\rm ext}
 =\lambda_x+\varrho_x+E_{1,x}+E_{2,x}
  -22-2h_x-2i_x.
\tag{6.4}
\]

### Theorem 3 — literal/repeat external-capacity inequalities

Every \(n_5=133\) zero-margin survivor must satisfy, for every coordinate
\(x\),

\[
\boxed{
 \ell_x^{(5)}+\lambda_x
 \le90+n_4+R_x^{(3)}+h_x,
}
\tag{6.5}
\]

\[
\boxed{
 \ell_x^{(5)}+2\lambda_x+\varrho_x+E_{1,x}+E_{2,x}
 \le155+n_4+2h_x+2i_x,
}
\tag{6.6}
\]

and

\[
\boxed{
 \varrho_x+E_{1,x}+E_{2,x}
 \le
 3\ell_x^{(5)}+2\lambda_x+3b_x
 +22+2h_x+2i_x.
}
\tag{6.7}
\]

The long-zero-tail inequality also has the rank-four form

\[
\boxed{
 \varrho_x+E_{1,x}+2E_{2,x}+3R_x^{(3)}
 \ge66-n_4+h_x+i_x,
}
\tag{6.8}
\]

or, equivalently,

\[
\boxed{
 E_{2,x}+2R_x^{(3)}
 \ge1+\lambda_x-n_4-i_x.
}
\tag{6.9}
\]

### Proof

Substitute (6.2) and (6.1) into the anchor capacity (5.9).  This gives

\[
 43-R_x^{(3)}-h_x
 \le133+n_4-\ell_x^{(5)}-\lambda_x,
\]

which is (6.5).

Substitute (6.4) into

\[
 e_x^{\rm ext}\le E-a_x
\]

and use (6.1)--(6.2).  Rearrangement gives (6.6).

Similarly, substitute (6.3)--(6.4) into the directed exposure inequality

\[
 e_x^{\rm ext}\le3u_{\{x\}}
\]

to obtain (6.7).

The central occurrence identity is

\[
 o_x=56-h_x-i_x+\varrho_x.
\tag{6.10}
\]

Partitioning all zero positions among the runs gives

\[
 K_x
 =m-o_x-E_{1,x}-2E_{2,x}-3R_x^{(3)}.
\tag{6.11}
\]

Insert (6.1) and (6.10) into \(K_x\le210\).  This is exactly (6.8).

Finally, the audited rank-four budget

\[
 E_{1,x}+E_{2,x}+R_x^{(3)}+\lambda_x+\varrho_x
 =65+h_x+2i_x
\tag{6.12}
\]

reduces (6.8) to (6.9).  ∎

## 7. Why these capacities do not yet contradict a template

The new theorem genuinely fixes the external gate at the correct level:

* (3.4) is the exact Hall capacity for the prescribed extension-label
  vector against the actual external sources;
* \(d_X\) is the additional physical one-sided-offset capacity;
* (3.5) forces every missing central subset completion into those same
  exposed labels; and
* (6.6)--(6.9) connect that capacity to the rank-four literal/repeat
  ledger.

Nevertheless, the currently audited scalar data leave substantial slack.
The reason can now be stated precisely.

First, the subset-star lower bound (4.6) disappears for every
\(|X|\ge2\), because \(E\ge132>126=u_2\).  Thus the full hierarchy cannot
be collapsed to another positive rankwise inequality.

Second, at \(n_5=133\), the rank-four ledger fixes
\(\lambda_x,\varrho_x,E_{1,x},E_{2,x},R_x^{(3)}\) only through the displayed
relations, while the literal rank-five incidence vector
\(\ell_x^{(5)}\) and the six-cell boundary vector \(b_x\) remain free.
Those are exactly the two vectors which control the anchor and directed
exposure capacities in (6.6)--(6.7).

Third, summing the anchor capacities has large unavoidable slack.  The
external anchors have total coordinate incidence

\[
 \sum_x a_x=5\cdot133+4n_4,
\]

whereas every anchor omits six or seven coordinates.  The total external
label demand is only \(E=133+n_4\).  A contradiction therefore has to be
set-valued or order-sensitive; it cannot follow from the eleven capacities
after summation.

The exact next gate is consequently:

> control the actual literal rank-five source family and the directed
> three-cell exposure sets strongly enough to violate (3.4) for some
> coordinate set \(X\), while simultaneously respecting the central
> completion lower bound (3.5).

This is strictly narrower than the previous free external-label problem,
but the available rank-four and run ledgers alone do not settle it.

## 8. Self-audit

The proof uses only the following audited inputs:

1. the word has \(465\) positions in the zero-margin template;
2. the selected rank-five and rank-six intervals have ordered endpoints and
   physical length at most four;
3. endpoint saturation pairs every external left or right endpoint at the
   same physical position and makes the rank-five interval a proper
   subinterval of the rank-six interval;
4. the central rank-five witnesses are all triple windows except \(H\), and
   the central rank-six witnesses are all four-windows;
5. the full matching completes every \(t\)-set exactly \(\Delta_t\) times;
6. the exact central/external label law (5.7); and
7. for Section 6 only, the audited \(n_5=133\) rank-four identities.

No step assumes that separately chosen subset marginals can be glued.  The
same external matching edge, source, upper set, label, anchor, and added
cell block are used throughout.

The factor \(3\) in (3.4) is literal: an added coordinate lies within three
positions of its saturated outer endpoint, and one physical occurrence can
be reached from at most three such endpoints.  It is not an average or an
asymptotic estimate.

The \(210\) in (5.8) has two independent exact derivations, from source
Hall capacity and from the complete rank-six point degree.  Their equality
is an audit of all endpoint and seam constants.

No contradiction to a zero-margin survivor, and hence no improvement to
the current interval for \(\nu(11)\), is claimed.

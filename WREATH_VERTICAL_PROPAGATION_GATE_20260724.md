# Vertical propagation for exact wreath shadows: exact ledger and a no-go theorem

## Verdict

Let

\[
n=2m+1,\qquad W=\binom nm,
\]

and let \(\mathcal F\) be an exact middle wreath factor.  Write

\[
\mathcal A_q=\bigcup_{\pi\in\mathcal F}
 \{I_\pi(j,m-q):j\in\mathbb Z_n\},\qquad
N_q=\binom n{m-q},
\]

\[
a_q=|\mathcal A_q|=N_q-M_q.
\]

There is an exact adjacent-depth expansion ledger for the defects.  It
reduces the weak vertical wreath lemma to controlling the loss of distinct
labels at the transitions \(q-1\to q\), and it allows later overexpansion to
repair an earlier loss.

There is **no deterministic propagation theorem from shallow support sizes
and the mandatory one-step support-neighbour conditions alone**.  At that
relaxed support level one can have

* exact coverage at depth \(1\) and at every odd checkpoint depth;
* positive-density holes at every even depth; and
* at least two covered immediate lower and upper neighbours for every
  covered checkpoint label.

Thus neither \(M_1=o(W)\), nor even perfect alternate-depth checkpoint
coverage, can imply the weak vertical wreath lemma by containment,
endpoint-degree, or support expansion alone.  A successful propagation
theorem must use coherent ownership of occurrences across two or more
successive depths (or an equivalent global cyclic-order statistic).

The countermodel below is a support model, not an exact wreath factor.  It
therefore does not disprove the weak vertical wreath lemma.  It proves that
the missing ingredient cannot be eliminated by a deterministic inequality
using only the currently visible adjacent support data.  The certified
\(m=4\) exact factor with \(M_1=0\) and \(M_2=2\) shows that the qualitative
failure already occurs inside the actual wreath class.

## 1. Exact vertical support-expansion ledger

Put

\[
\tau_q:=\frac{N_q}{N_{q-1}}
=\frac{m-q+1}{m+q+1},\qquad
\kappa_q:=\frac{a_q}{a_{q-1}}\qquad(1\le q<m).
\]

Define the normalized support loss

\[
Y_q:=\log\frac{N_q}{a_q}
=-\log\left(1-\frac{M_q}{N_q}\right),
\qquad Y_0=0.
\]

### Theorem 1 (vertical expansion identity)

For every exact middle wreath factor and every \(q<m\),

\[
\boxed{Y_q-Y_{q-1}=\log\frac{\tau_q}{\kappa_q}.}
\tag{1.1}
\]

Consequently, if

\[
L_i:=\log\frac{\tau_i}{\kappa_i},\qquad
\rho_q:=\frac{N_q}{W},
\]

then all partial sums are nonnegative,

\[
Y_q=\sum_{i=1}^qL_i\ge0,
\tag{1.2}
\]

and the complete weak-wreath defect has the exact form

\[
\boxed{
\frac1W\sum_{q=1}^H M_q
=\sum_{q=1}^H\rho_q
 \left(1-\exp\left[-\sum_{i=1}^qL_i\right]\right).}
\tag{1.3}
\]

In particular, with

\[
R_i:=\sum_{q=i}^H\rho_q,
\]

the following are sufficient for \(\sum_{q\le H}M_q=o(W)\):

\[
\sum_{q=1}^H\rho_qY_q=o(1),
\tag{1.4}
\]

or the stronger local condition

\[
\boxed{
\sum_{i=1}^H R_i(L_i)_+=o(1).}
\tag{1.5}
\]

### Proof

The first identity is just the quotient of successive normalized support
sizes:

\[
Y_q-Y_{q-1}
=\log\frac{N_q}{N_{q-1}}
 -\log\frac{a_q}{a_{q-1}}
=\log\frac{\tau_q}{\kappa_q}.
\]

Summing gives (1.2).  Since \(a_q/N_q=e^{-Y_q}\),

\[
\frac{M_q}{W}
=\frac{N_q}{W}\left(1-\frac{a_q}{N_q}\right)
=\rho_q(1-e^{-Y_q}),
\]

which proves (1.3).  The inequality \(1-e^{-y}\le y\) for \(y\ge0\)
shows that (1.4) is sufficient.  Finally,

\[
\sum_{q=1}^H\rho_qY_q
=\sum_{i=1}^H R_iL_i
\le\sum_{i=1}^H R_i(L_i)_+,
\]

proving (1.5).  Notice that the signed identity permits a later transition
with \(\kappa_i>\tau_i\) to repair an earlier support loss.  \(\square\)

### Quantitative weights in the tail-compatible range

The exact product

\[
\rho_q=\prod_{t=1}^q\frac{m-t+1}{m+t+1}
\]

gives

\[
\rho_q\le
\exp\left(-\frac{q(q+1)}{m+q+1}\right)
\le \exp\left(-\frac{q^2}{2m+1}\right).
\tag{1.6}
\]

Therefore

\[
R_i\le C\sqrt m\exp\left(-\frac{(i-1)^2}{4m+2}\right),
\tag{1.7}
\]

and also

\[
\sum_{i=1}^H R_i
=\sum_{q=1}^Hq\rho_q=O(m).
\tag{1.8}
\]

Thus (1.5) is a genuinely weighted local target: losses near the middle are
expensive, while losses near the tail cutoff have Gaussian-small weight.
For example, the uniform condition \((L_i)_+=o(1/m)\) is sufficient, though
far stronger than necessary.

### Theorem 2 (split--merge collision ledger)

The logarithmic ledger has an exact integral version which retains the
common ownership of pointed wreath starts.

Let

\[
\Omega=\{(\pi,j):\pi\in\mathcal F,\ j\in\mathbb Z_n\},
\qquad |\Omega|=W,
\]

and put

\[
X_q(\pi,j)=I_\pi(j,m-q).
\]

For \(1\le q\le H\), form the **simple** bipartite transition graph
\(G_q\): its left vertices are the labels in \(\mathcal A_{q-1}\), its
right vertices are the labels in \(\mathcal A_q\), and it contains the
edge \((T,S)\) when

\[
(X_{q-1}(\omega),X_q(\omega))=(T,S)
\]

for at least one \(\omega\in\Omega\).  Parallel occurrences are suppressed.
Write

\[
e_q=|E(G_q)|,\qquad
s_q=e_q-a_{q-1},\qquad
t_q=e_q-a_q.
\tag{1.9}
\]

Every vertex of \(G_q\) is incident with an edge, so \(s_q,t_q\ge0\).
The quantity \(s_q\) is the distinct-child **split surplus**, while
\(t_q\) is the distinct-parent **merge surplus**.  Put

\[
\Delta_q=N_{q-1}-N_q.
\]

If

\[
\mu_q(S)=|\{\omega:X_q(\omega)=S\}|,
\qquad D_q=\sum_S(\mu_q(S)-1)_+=W-a_q,
\]

then the transition surpluses obey the exact occurrence-reservoir bounds

\[
\boxed{s_q\le D_{q-1},\qquad t_q\le D_q.}
\tag{1.10}
\]

Indeed, the distinct outdegree of a parent label is at most its occurrence
multiplicity, and the distinct indegree of a child label is at most its
occurrence multiplicity.

Then

\[
\boxed{M_q-M_{q-1}=t_q-s_q-\Delta_q.}
\tag{1.11}
\]

Consequently,

\[
\boxed{
\sum_{q=1}^H M_q
=\sum_{i=1}^H(H-i+1)(t_i-s_i-\Delta_i).}
\tag{1.12}
\]

All partial sums of the increments in (1.11) are nonnegative.  In
particular, the following local transition condition is sufficient for
(WV):

\[
\boxed{
\sum_{i=1}^H(H-i+1)
 (t_i-s_i-\Delta_i)_+=o(W).}
\tag{1.13}
\]

#### Proof

Since

\[
a_q-a_{q-1}=(e_q-t_q)-(e_q-s_q)=s_q-t_q,
\]

we have

\[
\begin{aligned}
M_q-M_{q-1}
&=(N_q-N_{q-1})-(a_q-a_{q-1})\\
&=-\Delta_q-s_q+t_q,
\end{aligned}
\]

which is (1.11).  Summing first in \(i\le q\), and then over
\(q\le H\), gives (1.12).  Dropping negative increments gives (1.13).
\(\square\)

At depth one, every middle label has a unique pointed occurrence.  Hence
\(e_1=W\), \(s_1=0\), and

\[
t_1=W-a_1.
\]

Equation (1.11) becomes

\[
M_1=(W-a_1)-(W-N_1),
\]

which is exactly the known collision ledger: total repeat occurrences minus
the unavoidable overlap.  At later depths a repeated parent label can split
into several distinct child transition types; the term \(s_q\) is the
precise repair mechanism missing from any attempted propagation based only
on \(M_{q-1}\).

## 2. A universal one-step support inequality is weak

Every occurrence of an \(r\)-interval has two distinct endpoint deletions,
both of which are \((r-1)\)-intervals in the same cyclic order.  Hence every
label in \(\mathcal A_{q-1}\) contains at least two labels in
\(\mathcal A_q\).  A fixed \((r-1)\)-set has at most \(n-r+1\) rank-\(r\)
supersets.  Double counting distinct containment incidences gives

\[
2a_{q-1}\le(m+q+1)a_q,
\tag{2.1}
\]

where \(r=m-q+1\).  Equivalently,

\[
\kappa_q\ge\frac2{m+q+1}.
\tag{2.2}
\]

This is far too weak on the vertical scale: the ideal ratio
\(\tau_q\) is \(1-O(q/m)\), whereas (2.2) permits a one-step loss by a
factor of order \(m\).  The next theorem shows that this weakness is not an
artifact of the double count.  Even positive-density one-step loss is
compatible with every bidirectional minimum-degree consequence of endpoint
geometry.

## 3. Dense two-sided funnel families

The following theorem is stated in the central regime needed for the weak
vertical wreath lemma.

### Theorem 3 (dense alternating support countermodel)

Fix a constant \(0<p<1/4\), and let \(H=H(m)=o(m)\).  For all sufficiently
large \(m\), there are families

\[
\mathcal B_q\subseteq\binom{[2m+1]}{m-q},
\qquad 0\le q\le H,
\]

with the following properties.

1. \(\mathcal B_0\) and every odd-depth family are complete:

   \[
   \mathcal B_0=\binom{[2m+1]}m,
   \qquad
   \mathcal B_q=\binom{[2m+1]}{m-q}\quad(q\text{ odd}).
   \tag{3.1}
   \]

2. At every even depth \(q\ge2\),

   \[
   \left|\binom{[2m+1]}{m-q}\setminus\mathcal B_q\right|
   =(p+o(1))\binom{2m+1}{m-q}.
   \tag{3.2}
   \]

3. Every member of \(\mathcal B_q\) has at least two covered immediate
   subsets in \(\mathcal B_{q+1}\), whenever \(q<H\), and at least two
   covered immediate supersets in \(\mathcal B_{q-1}\), whenever \(q>0\).

Consequently, depth \(1\) and all odd checkpoint depths are perfect, all
mandatory adjacent support degrees are present, but for every
\(H\ge\lfloor\sqrt m\rfloor\),

\[
\sum_{q=1}^H
\left(\binom{2m+1}{m-q}-|\mathcal B_q|\right)
=\Theta(W\sqrt m).
\tag{3.3}
\]

In particular it is not \(o(W)\).

### Proof

Only the even-depth families need to be constructed.  Fix such a depth
\(q\) and put \(r=m-q\).  Choose a random hole family

\[
\mathcal H_q\subseteq\binom{[n]}r,
\qquad n=2m+1,
\]

by including every \(r\)-set independently with probability \(p\), and set

\[
\mathcal B_q=\binom{[n]}r\setminus\mathcal H_q.
\]

Consider a fixed \((r+1)\)-set \(T\).  It fails to contain two members of
\(\mathcal B_q\) only if at least \(r\) of its \(r+1\) facets are holes.
The probability of this event is at most

\[
(r+2)p^r.
\tag{3.4}
\]

Similarly, a fixed \((r-1)\)-set \(S\) has

\[
d=n-r+1
\]

rank-\(r\) supersets.  It fails to have two supersets in \(\mathcal B_q\)
only if at least \(d-1\) of them are holes, an event of probability at most

\[
(d+1)p^{d-1}.
\tag{3.5}
\]

There are fewer than \(2^n\) possible sets of either kind.  Uniformly for
\(q\le H=o(m)\), both \(r\) and \(d\) equal \((1+o(1))m\).  Since

\[
2\log2+\log p<0,
\]

the union of all events (3.4)--(3.5), over every relevant set and every
even \(q\le H\), has probability \(o(1)\).  Chernoff's inequality, again
uniformly over the \(O(H)\) ranks, gives

\[
|\mathcal H_q|=(p+o(1))\binom nr.
\]

Thus a simultaneous choice satisfying (3.1)--(3.2) and both neighbour
conditions exists.

For \(q\le\sqrt m/2\), the exact product for \(N_q/W\) is bounded below by
an absolute positive constant.  There are \(\Theta(\sqrt m)\) even depths
in this range, so (3.2) gives the lower bound in (3.3).  The Gaussian upper
bound (1.6) gives

\[
\sum_{q\ge1}N_q=O(W\sqrt m),
\]

and hence gives the matching upper bound.  This proves (3.3).  \(\square\)

## 4. What Theorem 3 rules out

For actual cyclic intervals, the two immediate endpoint deletions and the
two immediate one-element extensions are distinct.  Therefore item 3 of
Theorem 3 contains every one-step statement about **which target labels are
present** that follows merely from this endpoint geometry.

The theorem consequently rules out each of the following proof forms.

* \(M_1=o(W)\) plus endpoint containment implies all deeper defects are
  \(o(W)\).
* Exact injectivity at alternating or sparse checkpoint depths forces the
  omitted depths.
* Minimum degree two in every adjacent shadow-incidence graph is enough to
  interpolate the band.
* A deterministic inequality involving only the support cardinalities
  \(a_q\) and the existence of endpoint neighbours can prove (WV).

This is stronger than the isolated two-sided funnel: it permits
positive-density holes at \(\Theta(\sqrt m)\) depths simultaneously while
all alternate checkpoints are exact.

It does **not** rule out a theorem using the common occurrence set

\[
\Omega=\{(\pi,j):\pi\in\mathcal F,\ j\in\mathbb Z_n\}
\]

and the fact that the same \(\omega\in\Omega\) carries one nested interval
through every depth.  The support model deliberately forgets this ownership.
That is now the exact missing datum.

## 5. A smaller valid target than arbitrary multidepth Hall matching

Theorem 1 yields the following sufficient replacement target.

### Corollary 3 (weighted loss-transition criterion)

For the tail-compatible cutoff

\[
H=\left\lceil(1/2+\varepsilon)
\sqrt{(2m+1)\log(2m+1)}\right\rceil,
\]

it suffices to construct an exact middle wreath factor for which

\[
\boxed{
\sum_{i=1}^H
\left(\sum_{q=i}^H\frac{\binom{2m+1}{m-q}}{W}\right)
\left[
\log\frac{(m-i+1)a_{i-1}}{(m+i+1)a_i}
\right]_+=o(1).}
\tag{5.1}
\]

Only transitions at which the distinct support contracts faster than the
binomial layer need be paid for.  A later overexpanding transition is a real
repair in the exact signed ledger (1.3), though (5.1) conservatively ignores
that cancellation.

This criterion is not claimed to be easier than (WV) in every construction.
Its value is diagnostic: after Theorem 3, any valid attempt to derive (5.1)
must use multi-step occurrence coherence, trades preserving common middle
ownership, or an explicit cyclic-order recursion.  Shallow defect counts and
adjacent target supports contain insufficient information.

## 6. Exact status

Proved here:

* the exact vertical support-expansion identity (1.1)--(1.3);
* the weighted local sufficient criterion (1.5)/(5.1);
* a positive-density alternating-depth countermodel satisfying every
  bidirectional one-step support requirement;
* therefore, a no-go theorem for deterministic shallow-defect propagation
  based only on adjacent supports.

Not proved here:

* realization of the countermodel by an exact wreath factor;
* a lower bound showing that every exact wreath factor must have such holes;
* the occurrence-coherent expansion estimate (5.1);
* the weak vertical wreath lemma or the constant-one OR upper bound.

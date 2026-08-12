# Hybrid adaptive-MTF / refined-rotor fusion

Date: 2026-07-25

## 0. Verdict

This route does **not** prove the contiguous-OR width conjecture. It does
produce three unconditional advances.

1. Every Johnson path, with arbitrary positive re-entries, has a literal
   tail-insensitive radius-\(H\) MTF lift. A re-entry whose next-exit
   priority is \(j\) has an explicit portal of length \(H-j+1\), sharp for
   the prescribed chronological priority prefix, rather than requiring an
   isolated reset.
2. The total portal excess is not a new independent error term. It is
   exactly the total number of loops in the common lower projections. An
   Euler identity for those projected graphs gives an exact
   portal--defect--cycle ledger. In particular, below
   \(H=o(m^{1/3})\), aggregate lower support defect
   \(\sum_{q\le H}M_q^-=o(W)\) automatically implies portal excess \(o(W)\),
   provided the component and duplicate ledgers are also \(o(W/H)\).
3. Recoalescing the stale tail is impossible at coefficient one. Between
   two distinct minimal radius-\(H\) fibres the exact portal distance is at
   least \(2H+1\), and this forces length \(2W-o(W)\) when
   \(H\to\infty\), \(H=o(\sqrt m)\), if all (or \(W-o(W)\)) middle masks are
   witnessed at minimal endpoints. Persistent extra-block memory is
   therefore necessary, not cosmetic.

The new construction is not the complete-state bridge theorem
\(\mathrm{PTAD}_A\). Its vertices are refined-prefix cylinders; the tail is
deliberately left split, and every transition is valid for every such tail.

The exact unresolved global issue is common decorated ownership. One must
choose one chronology (or one correlated endpoint path cover) for which the
endogenous lower and upper flags have aggregate defect \(o(W)\). Separate
rankwise choices, a cover of undecorated Boolean supports, or recomputing
the future queue after independent epochs have been selected do not supply
this.

Throughout,

\[
 \Omega=[2m],\qquad W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.
\tag{0.1}
\]

All word entries are nonempty subsets of \(\Omega\).

---

## 1. Last-occurrence states

For an ordered partition

\[
 \Pi=(B_1,\ldots,B_s)
\]

and a nonempty set \(X\subseteq\Omega\), write

\[
 M_X(\Pi)=(X,B_1\setminus X,\ldots,B_s\setminus X),
\tag{1.1}
\]

deleting empty blocks. This is the complete last-occurrence update.

### Lemma 1.1 (endpoint-prefix lemma)

After any word position \(t\), every interval union ending at \(t\) is a
prefix union of the complete last-occurrence state at \(t\). Consequently,
one word position can represent at most one set of any prescribed rank.

#### Proof

Two coordinates are in the same state block precisely when their last
occurrence times up to \(t\) agree. For \(i\le t\), the union of the word
entries from \(i\) through \(t\) is the set of coordinates whose last
occurrence time is at least \(i\). This is a union of the newest state
blocks, hence a prefix union. Prefix sizes strictly increase, proving the
last assertion. \(\square\)

### Lemma 1.2 (block-count identity)

If \(b(\Pi)\) is the number of blocks of \(\Pi\), then

\[
 b(M_X\Pi)
 =1+b(\Pi)-\#\{B\in\Pi:B\subseteq X\}.
\tag{1.2}
\]

#### Proof

The new block \(X\) contributes one. An old block survives exactly when it
is not contained in \(X\). \(\square\)

---

## 2. Refined priority cylinders

Fix \(1\le H\le m-1\). A radius-\(H\) refined cylinder is the family of
complete ordered partitions beginning

\[
 \widehat\Pi=
 \bigl(
 L,\{x_{H-1}\},\ldots,\{x_0\},
 \{y_1\},\ldots,\{y_H\},B_1,\ldots,B_s
 \bigr),
\tag{2.1}
\]

where \(|L|=m-H\), all displayed coordinates are distinct, and the
nonempty \(B_\nu\) partition the remaining coordinates. Its middle owner
and common signed flags are

\[
 T=L\cup\{x_0,\ldots,x_{H-1}\},
\tag{2.2}
\]

\[
 A_q^-(\widehat\Pi)
 =L\cup\{x_q,\ldots,x_{H-1}\},
 \qquad 1\le q\le H,
\tag{2.3}
\]

and

\[
 A_q^+(\widehat\Pi)
 =T\cup\{y_1,\ldots,y_q\},
 \qquad 1\le q\le H.
\tag{2.4}
\]

Only the displayed prefix is prescribed. No assertion is made that the
older tail is one block.

### Theorem 2.1 (sharp priority-prefix portal)

Let

\[
 T'=T-\{x_0\}+\{a\},\qquad a\notin T.
\tag{2.5}
\]

There are two cases.

**Nonqueued arrival.** Suppose \(a\) is outside the prescribed \(H\)
earliest future departures at \(T'\). Let \(b\in L\) be the next old
coordinate entering that queue. The single update

\[
 X=(L-\{b\})\cup\{a\}
\tag{2.6}
\]

produces a state beginning

\[
 \bigl(
 L-b+a,\{b\},\{x_{H-1}\},\ldots,\{x_1\},\{x_0\},
 \text{surviving upper blocks}
 \bigr).
\tag{2.7}
\]

Its priority excess over one ordinary Johnson transition is zero.

**Queued arrival.** Suppose the target future-departure queue is

\[
 (x_1,\ldots,x_j,a,x_{j+1},\ldots,x_{H-1}),
 \qquad 0\le j\le H-1,
\tag{2.8}
\]

where an empty displayed range is omitted. Then the word

\[
 \{a\},\{x_{j+1}\},\ldots,\{x_{H-1}\},L
\tag{2.9}
\]

has length

\[
 r=H-j+1
\tag{2.10}
\]

and produces the exact prefix

\[
 \bigl(
 L,\{x_{H-1}\},\ldots,\{x_{j+1}\},\{a\},
 \{x_j\},\ldots,\{x_1\},\{x_0\},
 \text{surviving upper blocks}
 \bigr).
\tag{2.11}
\]

Thus its priority excess is

\[
 \delta=r-1=H-j.
\tag{2.12}
\]

The length (2.10) is minimal among words reaching the prescribed target
priority prefix (2.11).

#### Proof

For (2.6), direct subtraction in (1.1) leaves \(\{b\}\) from the old core,
preserves the old lower singletons, removes \(a\) from whichever upper or
tail block contained it, and prepends \(L-b+a\). This is (2.7).

For (2.9), after the singleton updates, reverse recency order is

\[
 x_{H-1},\ldots,x_{j+1},a,
\]

followed by the untouched displayed blocks. The final update \(L\) gives
exactly (2.11). This calculation is unaffected by how the residual tail is
partitioned.

For minimality, \(a\) must be touched: initially it lies strictly below
\(x_0\), while in (2.11) it lies above \(x_j,\ldots,x_0\). After the last
touch of \(a\), the \(H-j\) distinct final blocks

\[
 L,\{x_{H-1}\},\ldots,\{x_{j+1}\}
\]

must receive distinct later last-occurrence times. Hence at least
\(1+(H-j)\) updates are necessary. The displayed word attains this.
\(\square\)

### Scope correction 2.2

The theorem reaches an **endogenous** upper queue: \(x_0\) becomes the new
first upper singleton and is followed by surviving old upper singletons.
It does not synchronize an independently prescribed target upper queue.

The word is also not a shortest path to an arbitrary saturated state over
\(T'\). Indeed, for any \(b\in L\), the one update \(L-b+a\) reaches some
saturated radius-\(H\) state over \(T'\). Sharpness in Theorem 2.1 is
sharpness for the chronological priority prefix, which is exactly the
sequential compatibility required below.

### Lemma 2.3 (re-entry and composition)

The two transitions in Theorem 2.1 are valid whether \(a\) lies in a
displayed upper singleton or in an arbitrary tail block, and they compose
indefinitely.

#### Proof

If \(a=y_k\), its old singleton is deleted and the departed \(x_0\) replaces
it, leaving exactly \(H\) advertised upper singletons. If \(a\) lies in the
later tail, all old \(H\) upper singletons survive; advertise the first
\(H\) among \(x_0,y_1,\ldots,y_H\), leaving the extra singleton in the
tail. In both cases the undisplayed blocks remain an ordered partition of
the new residual set. \(\square\)

### Lemma 2.4 (future-exit queues exist)

Every finite oriented Johnson path admits compatible priority lists of the
form used in Theorem 2.1.

#### Proof

Order each currently present coordinate by its next actual departure.
After the terminal vertex, choose a set \(D\) of \(H\) terminal coordinates
and give them distinct hypothetical departure slots \(1,\ldots,H\). For
any such \(D\) and any earlier middle set \(T_i\),

\[
 |T_i\setminus T_{\rm end}|+|T_i\cap D|\ge H,
\tag{2.13}
\]

because

\[
 |T_i\setminus T_{\rm end}|+|T_i\cap D|
 =m-|T_i\cap(T_{\rm end}\setminus D)|\ge H.
\]

Thus at least \(H\) future exits are available at every state.

The dummy set can be chosen without making any terminally persistent
arrival priority-active. Order the terminal coordinates
\(z_1,\ldots,z_m\) by increasing time of their last entry into the path,
putting coordinates present from the initial vertex first. Exclude the
latest \(z_m\), choose any \(H\) of the other coordinates for \(D\), and
dummy-depart the chosen coordinates in increasing last-entry order.

Fix a selected \(z_t\) with an internal last entry. Immediately after that
entry, the \(t\) terminal coordinates \(z_1,\ldots,z_t\) persist to the
end. The other \(m-t\) coordinates then present must actually depart before
the terminal vertex. Among \(z_1,\ldots,z_{t-1}\), at most
\(m-H-1\) are excluded from \(D\), because the excluded later coordinate
\(z_m\) already uses one of the \(m-H\) exclusions. Therefore at least

\[
 (m-t)+(t-1-(m-H-1))=H
\tag{2.14}
\]

contemporaries depart before the dummy departure of \(z_t\). Hence \(z_t\)
lies outside the \(H\)-priority queue at its entry. Unselected terminal
coordinates have no departure among the first \(H\) dummy slots, and
initial coordinates have no internal entry. Thus the completion introduces
no boundary priority toll.

Finally, the priority order changes from one state to the next only by
deleting \(x_0\) and inserting \(a\), yielding exactly (2.7) or (2.8).
Later re-entries do not affect the first future exit used in this ordering.
\(\square\)

### Corollary 2.5 (literal lift of an arbitrary Johnson path)

Let \(P=(T_0,\ldots,T_{K-1})\) be any oriented Johnson path. If \(j_i\) is
the target priority of an arrival that enters the target queue, put

\[
 J_H(P)=\sum_{i:\,a_i\text{ queued}}(H-j_i).
\tag{2.15}
\]

Then \(P\) has a literal refined-prefix word of exact length

\[
 \boxed{K+2H+J_H(P)}.
\tag{2.16}
\]

Every \(T_i\) owns one common nested signed radius-\(H\) flag, and for every
Johnson edge \(T_iT_{i+1}\),

\[
 A^-_{i,1}=T_i\cap T_{i+1},\qquad
 A^+_{i+1,1}=T_i\cup T_{i+1}.
\tag{2.17}
\]

#### Proof

Initialize the useful prefix by writing

\[
 \{y_H\},\ldots,\{y_1\},
 \{x_0\},\ldots,\{x_{H-1}\},L.
\tag{2.18}
\]

This takes \(2H+1\) entries and its last entry already marks \(T_0\), so
the initialization excess is \(2H\). Every later center costs one ordinary
transition plus its priority excess. Summing gives (2.16). Equations
(2.3), (2.7), and (2.11) give (2.17). \(\square\)

The priority \(j_i\) is an order statistic, not generally the elapsed
length of the positive run of \(a_i\). It counts the coordinates present
immediately after \(a_i\) enters whose **first future departures** occur
before the first future departure of \(a_i\). Later arrivals which depart
before \(a_i\) do not contribute to \(j_i\).

With the zero-toll terminal completion in Lemma 2.4, if
\(\mathcal A_H(P)\) is the set of internal arrivals whose next actual
departure has contemporaneous rank \(j_i<H\), then exactly

\[
 \boxed{
 J_H(P)=\sum_{i\in\mathcal A_H(P)}(H-j_i).}
\tag{2.19}
\]

---

## 3. A necessary correction to run-length cutting

The priority construction is genuinely different from the former
short-run transversal.

### Proposition 3.1 (run length does not determine portal cost)

There is a Johnson path on which an arrival exits three transitions later
but has target priority \(j=1\), rather than \(j=2\).

#### Proof

For \(m=4\), take

\[
 \{p,x,u,v\}
 \xrightarrow{p\to a}
 \{a,x,u,v\}
 \xrightarrow{x\to b}
 \{a,b,u,v\}
 \xrightarrow{b\to c}
 \{a,c,u,v\}
 \xrightarrow{a\to p}\cdots .
\tag{3.1}
\]

Only \(x\), among the coordinates present immediately after \(a\) entered,
has its first future departure before that of \(a\). Thus \(j=1\), although
the elapsed return length is three. \(\square\)

For \(H=3\), Theorem 2.1 charges excess \(H-j=2\), whereas the false
run-length formula would charge \(H-3+1=1\).

For each \(R\in\mathcal A_H(P)\), let \(I_R\) be the path-edge interval
from its entry edge through its next exit edge, inclusive, and put

\[
 w_R=H-j_R.
\tag{3.2}
\]

These active intervals can be arbitrarily long and arbitrarily nested.

### Theorem 3.2 (exact hybrid priority-cut identity)

Within the architecture marking every retained middle center by its
chronological priority cylinder, the minimum literal length obtainable by
cuts and priority portals is

\[
 K+2H+\Phi_H(P),
\tag{3.3}
\]

where

\[
 \boxed{
 \Phi_H(P)=
 \min_C
 \left(
 2H|C|+
 \sum_{\substack{R\in\mathcal A_H(P)\\I_R\cap C=\varnothing}}w_R
 \right).}
\tag{3.4}
\]

Its linear program has the exact dual

\[
 \boxed{
 \Phi_H(P)=
 \max\left\{
 \sum_R\alpha_R:
 0\le\alpha_R\le w_R,\quad
 \sum_{R:e\in I_R}\alpha_R\le2H
 \text{ for every edge }e
 \right\}.}
\tag{3.5}
\]

#### Proof

If \(I_R\cap C=\varnothing\), the entire entry-to-exit segment remains in
one fragment. Its contemporaneous first-exit rank \(j_R\), and hence its
portal cost \(w_R\), are unchanged by cuts outside that interval.

If a cut meets \(I_R\), the entry and next exit are not both internal to
one fragment. At an entry-side terminal boundary, use the zero-toll dummy
completion from Lemma 2.4; on the other side the coordinate is initially
present and creates no arrival toll. Thus a hit interval contributes zero.

The cuts create \(1+|C|\) fragments and therefore add \(2H|C|\) beyond the
original initialization excess \(2H\). This proves (3.4).

Equivalently, introduce cut variables \(z_e\) and paid-portal variables
\(u_R\):

\[
 \min\left\{
 2H\sum_e z_e+\sum_Rw_Ru_R:
 u_R+\sum_{e\in I_R}z_e\ge1,\quad
 z_e,u_R\in\{0,1\}
 \right\}.
\tag{3.6}
\]

The incidence matrix of intervals against points of a line is totally
unimodular by the consecutive-ones property; adjoining the identity
columns for the \(u_R\) preserves total unimodularity. The linear
relaxation is integral, and its dual is (3.5). \(\square\)

Because the primal matrix is totally unimodular and all costs and right
hand sides are integral, an optimal dual may also be chosen integral.

If \(\tau_H^{\rm pri}(P)\) is the minimum number of cuts meeting every
active priority interval, then

\[
 \Phi_H(P)\le
 \min\{J_H(P),\,2H\tau_H^{\rm pri}(P)\}.
\tag{3.7}
\]

This is not the former short-run transversal: its weights are first-exit
ranks \(H-j_R\), not \(H-|R|+1\), and its active intervals need not be
short. The projected-loop identity below is an independent exact
amortization of the same portal cost.

---

## 4. The exact portal--projection identity

Consider a forest \(\mathcal P\) of compatible marked radius-\(H\)
cylinders. Assume:

- there are \(T=W+D_0\) marked middle occurrences;
- every middle mask occurs at least once;
- the forest has \(C\) components;
- \(M_q^\pm\) is the number of signed rank-\(m\pm q\) masks absent from
  the marked-cylinder flags.

For each \(q\), project every marked occurrence to its lower flag \(A_q^-\)
and every forest edge to the corresponding edge between lower labels.
This gives a multigraph \(\Gamma_q^-\), with loops and parallel edges
retained. Let

\[
 \ell_q=\#\{\text{loops of }\Gamma_q^-\}.
\tag{4.1}
\]

Delete the loops but retain isolated used vertices. Let \(d_q\) be the
number of connected components of the resulting graph and let

\[
 \beta_q=
 \#\{\text{nonloop edges}\}
 -(N_q-M_q^-)+d_q
\tag{4.2}
\]

be its cyclomatic number. Finally put

\[
 \mu_q=C-d_q.
\tag{4.3}
\]

Both \(\beta_q\) and \(\mu_q\) are nonnegative. The first assertion is the
usual forest-versus-cycle identity. For the second, the image of each
original path component is connected, while images of different components
may merge, so \(d_q\le C\).

### Lemma 4.1 (one portal equals its lower loops)

For a nonqueued transition, no lower projection is a loop. For a
priority-\(j\) portal, the lower projection is a loop exactly at depths

\[
 q=j+1,\ldots,H.
\tag{4.4}
\]

Consequently,

\[
 \boxed{J=\sum_{q=1}^H\ell_q,}
\tag{4.5}
\]

where \(J\) is total priority excess.

#### Proof

In the nonqueued case, put \(x_H=b\). Directly from (2.3) and (2.7),

\[
 (A_q^-)'=A_q^--\{x_q\}+\{a\},
 \qquad 1\le q\le H.
\tag{4.6}
\]

Every projected edge is nonloop.

For a priority-\(j\) transition, (2.11) gives

\[
 (A_q^-)'=
 \begin{cases}
 A_q^--\{x_q\}+\{a\},&q\le j,\\[2mm]
 A_q^-,&q\ge j+1.
 \end{cases}
\tag{4.7}
\]

It therefore contributes one loop at exactly \(H-j\) depths, equal to its
priority excess. Summing over forest edges proves (4.5). \(\square\)

### Theorem 4.2 (exact priority-excess ledger)

For every \(1\le q\le H\),

\[
 \boxed{
 M_q^-=
 \ell_q+\beta_q+\mu_q-(D_0+W-N_q).}
\tag{4.8}
\]

Hence

\[
 \boxed{
 J=
 HD_0+\sum_{q=1}^H(W-N_q+M_q^-)
 -\sum_{q=1}^H(\beta_q+\mu_q).}
\tag{4.9}
\]

In particular,

\[
 \boxed{
 J\le
 HD_0+\sum_{q=1}^H(W-N_q)+\sum_{q=1}^HM_q^-.}
\tag{4.10}
\]

#### Proof

The projected multigraph has

\[
 T-C
\]

edge occurrences and \(N_q-M_q^-\) used vertices. After loops are removed,
(4.2) says

\[
 \beta_q=(T-C-\ell_q)-(N_q-M_q^-)+d_q.
\tag{4.11}
\]

Substitute \(T=W+D_0\) and \(d_q=C-\mu_q\), then rearrange. This is
(4.8). Sum (4.8) and use (4.5) to obtain (4.9). Dropping the nonnegative
\(\beta_q+\mu_q\) terms gives (4.10). \(\square\)

This identity is the promised exact portal-excess identity. In particular,
priority-active positive re-entries need not be entered as a separate reset
ledger: they are already encoded by loops of the same common lower flags
used for coverage.

### Lemma 4.3 (rank-gap estimate)

\[
 \boxed{
 \sum_{q=1}^H(W-N_q)
 \le
 \frac{H(H+1)(2H+1)}{6m}\,W.}
\tag{4.12}
\]

#### Proof

One has

\[
 \frac{N_q}{W}
 =\prod_{i=0}^{q-1}\frac{m-i}{m+i+1}.
\tag{4.13}
\]

For numbers \(0\le a_i\le1\),

\[
 1-\prod_i a_i\le\sum_i(1-a_i).
\]

Therefore

\[
 1-\frac{N_q}{W}
 \le
 \sum_{i=0}^{q-1}\frac{2i+1}{m+i+1}
 \le\frac{q^2}{m}.
\tag{4.14}
\]

Sum \(q^2\) from \(1\) to \(H\). \(\square\)

### Theorem 4.4 (literal band bound)

The cylinder forest has a literal OR word covering every rank
\(m-H,\ldots,m+H\) of length at most

\[
 \boxed{
 \begin{aligned}
 \mathcal L_{\rm band}\le {}&
 W+(H+1)D_0+2HC\\
 &+\frac{H(H+1)(2H+1)}{6m}W
 +2\sum_{q=1}^H M_q^-
 +\sum_{q=1}^H M_q^+ .
 \end{aligned}}
\tag{4.15}
\]

Consequently,

\[
 H=o(m^{1/3}),\qquad
 D_0=o(W/H),\qquad
 C=o(W/H),
\tag{4.16}
\]

and

\[
 \sum_{q=1}^H(M_q^-+M_q^+)=o(W)
\tag{4.17}
\]

imply

\[
 \mathcal L_{\rm band}=W+o(W).
\tag{4.18}
\]

#### Proof

A component with \(t\) marked centers has initialization excess \(2H\);
its transition excess is its contribution to \(J\). Thus the exact raw
length is

\[
 \mathcal L_{\rm raw}=T+2HC+J.
\tag{4.19}
\]

Append one literal copy of every signed band mask absent from the marked
flags. This costs at most

\[
 \sum_{q=1}^H(M_q^-+M_q^+).
\]

Now use \(T=W+D_0\), (4.10), and (4.12). Every term outside \(W\) is
\(o(W)\) under (4.16)--(4.17). \(\square\)

Initialization and portal-interior positions can themselves cover some
missing masks. Formula (4.15) deliberately ignores that bonus. If \(G\)
counts the distinct marked-flag holes represented anywhere at nonmarked raw
positions, the exact literal-completion policy has length

\[
 T+2HC+J+\sum_q(M_q^-+M_q^+)-G.
\tag{4.20}
\]

Here \(G\) must include initialization positions as well as portal
interiors.

### Corollary 4.5 (fusion of a first-band rainbow forest)

Suppose the \(W\) middle masks form a linear Johnson forest with \(e\)
edges whose lower and upper first-band colors are each globally distinct.
Then

\[
 C=W-e
 =(W-N_1)+(N_1-e)
 =\frac{W}{m+1}+(N_1-e).
\tag{4.21}
\]

Its priority lift preserves those colors by (2.17). Therefore, for
\(H=o(m^{1/3})\), the sufficient conditions reduce to

\[
 N_1-e=o(W/H)
\tag{4.22}
\]

and

\[
 \sum_{q=2}^H(M_q^-+M_q^+)=o(W).
\tag{4.23}
\]

Under (4.22)--(4.23), the forest gives a literal
\(W+o(W)\) band word without cutting its priority-active re-entries.

The importance of the range in (4.16) is structural: the **dynamical**
fusion theorem now works far beyond
\(o(\sqrt{\log m/\log\log m})\). What remains unproved at such depths is
the one-chronology support statement (4.23), not the MTF seam accounting.
The exponent \(1/3\) is only where the crude rank-gap upper bound (4.12)
becomes non-negligible; it is not a universal lower bound.

At Gaussian depth \(H=A\sqrt m\), (4.9), rather than (4.10), is the useful
form. Indeed,

\[
 \sum_{q\le A\sqrt m}(W-N_q)=\Theta_A(W\sqrt m).
\tag{4.24}
\]

Thus coefficient one would require the projected cycle/merge surplus
\(\sum_q(\beta_q+\mu_q)\) to cancel this baseline to within \(o(W)\).
The exact equality (4.9) isolates that additional Gaussian-window demand.

---

## 5. The constant-radius rotor state graph

The priority lift recomputes decorations from one global chronology. For
predecorated epochs, exact prefix compatibility is better expressed by the
following rotor graph.

Put \(r=m-H\). An abstract radius-\(H\) state is

\[
 \gamma=(L;z_1,\ldots,z_{2H};R),
 \qquad |L|=|R|=r,
\tag{5.1}
\]

where the displayed sets and coordinates partition \(\Omega\). Its flags
are

\[
 F_q^-(\gamma)=L\cup\{z_1,\ldots,z_{H-q}\},
\tag{5.2}
\]

\[
 F_q^+(\gamma)=L\cup\{z_1,\ldots,z_{H+q}\},
 \qquad 0\le q\le H.
\tag{5.3}
\]

Thus \(F_0^-=F_0^+\) is the middle owner.

For \(x\in L\) and \(y\in R\), define a directed rotor arc

\[
 \begin{aligned}
 &(L;z_1,\ldots,z_{2H};R)\\
 &\quad\longrightarrow
 (L-x+y;x,z_1,\ldots,z_{2H-1};R-y+z_{2H}).
 \end{aligned}
\tag{5.4}
\]

Every state has \(r^2\) outgoing and \(r^2\) incoming arcs.

### Theorem 5.1 (literal refined-tail lift)

Suppose the actual complete state begins

\[
 \widehat\Pi=
 (L,\{z_1\},\ldots,\{z_{2H}\},B_1,\ldots,B_s),
\tag{5.5}
\]

where the \(B_\nu\) partition \(R\). Appending

\[
 X=L-x+y
\tag{5.6}
\]

gives

\[
 \begin{aligned}
 M_X(\widehat\Pi)=(&X,\{x\},\{z_1\},\ldots,\{z_{2H}\},\\
                  &B_1-\{y\},\ldots,B_s-\{y\}),
 \end{aligned}
\tag{5.7}
\]

with empty blocks deleted. Its useful prefix is exactly the head of the
abstract rotor arc (5.4); the remaining blocks partition
\(R-y+z_{2H}\). Hence every finite abstract rotor path has a genuine
one-update-per-edge literal lift, with no tail recoalescence.

Moreover, if \(S=F_0(\gamma)\) and \(S'=F_0(\gamma')\), then

\[
 F_1^-(\gamma)=S\cap S',\qquad
 F_1^+(\gamma')=S\cup S'.
\tag{5.8}
\]

#### Proof

The update (5.6) contains every element of \(L\) except \(x\), contains
\(y\), and contains none of the \(z_i\). Formula (5.7) follows immediately
from (1.1). Grouping the undisplayed old singleton \(z_{2H}\) with the
remaining tail only at the abstract level gives the residual in (5.4).
No physical merge is asserted. Equations (5.2)--(5.4) give (5.8).
\(\square\)

### Proposition 5.2 (strong connectivity)

For \(1\le H\le m-2\), the directed rotor graph is strongly connected.

#### Proof

Temporarily order the elements of the two end blocks into slots

\[
 a_1,\ldots,a_r,q_1,\ldots,q_{2H},b_1,\ldots,b_r.
\]

Choosing the contents of \(a_i,b_j\) as \(x,y\) acts by the slot cycle

\[
 c_{ij}=(a_i,q_1,\ldots,q_{2H},b_j),
\tag{5.9}
\]

up to the harmless choice of left versus right action. Permutations within
the \(a\)-slots and within the \(b\)-slots do not change the abstract
state.

For \(r\ge2\),

\[
 c_{21}c_{11}^{-1}=(a_1,a_2,q_1).
\tag{5.10}
\]

Multiplication by the internal transposition \((a_1,a_2)\) gives
\((a_1,q_1)\). Conjugating by powers of \(c_{11}\) gives all adjacent
transpositions around the cycle

\[
 a_1,q_1,\ldots,q_{2H},b_1.
\]

Together with the internal end-block permutations, these generate
\(\operatorname{Sym}(\Omega)\), hence act transitively on abstract states.
Every \(c_{ij}\) has finite order \(2H+2\), so its inverse is a positive
power. Directed reachability therefore equals group reachability.
\(\square\)

The endpoint \(H=m-1\) has \(r=1\) and splits into cyclic-order orbits, so
the range in Proposition 5.2 is sharp.

---

## 6. Exact epoch fusion

Let \(\mathcal E\) be a finite family of decorated rotor epochs. An epoch
is a finite path in the graph (5.4), not merely the set of Boolean masks it
covers. Let \(D\) be the endpoint digraph on \(\mathcal E\): put
\(E\to E'\) when the terminal state of \(E\) has one rotor arc to the
initial state of \(E'\).

Write \(\operatorname{pc}(D)\) for the minimum number of vertex-disjoint
directed paths covering all epoch vertices.

### Theorem 6.1 (exact endpoint path-cover ledger)

If the epochs contain \(T\) center occurrences in total, then a minimum
path cover gives a literal refined-prefix word of exact raw length

\[
 \boxed{T+2H\,\operatorname{pc}(D).}
\tag{6.1}
\]

Moreover,

\[
 \boxed{
 \operatorname{pc}(D)=
 \min_{\prec}\max_{X\subseteq\mathcal E}
 \bigl(|X|-|\Gamma_\prec(X)|\bigr),}
\tag{6.2}
\]

where \(\prec\) ranges over total orders on the epochs and
\(\Gamma_\prec(X)\) is taken in the full right copy of \(\mathcal E\), with
\(u_Lv_R\) present exactly when \(u\to v\) in \(D\) and \(u\prec v\).
The choice \(X=\varnothing\) is allowed.

#### Proof

A rotor trail through \(t\) centers is initialized by its \(2H+1\) useful
blocks and then uses \(t-1\) one-step updates. Its exact length is
\(t+2H\). Summing over a path cover proves (6.1).

For a total order \(\prec\), split every epoch into a left and right copy
and retain only forward arcs. A matching of size \(\nu\) gives an acyclic
path cover with \(|\mathcal E|-\nu\) paths. Conversely, every directed path
cover admits a total order in which all its arcs are forward, and those arcs
form a matching of size \(|\mathcal E|-\operatorname{pc}(D)\). Thus

\[
 \operatorname{pc}(D)=
 \min_\prec\bigl(|\mathcal E|-\nu(D_\prec)\bigr).
\]

Hall's deficiency formula gives (6.2). \(\square\)

### Weighted extension 6.2

One may enlarge \(D\) by priority-prefix portals. Give a compatible arc
\(e\) the excess

\[
 \delta_e=r_e-1,
\tag{6.3}
\]

where \(r_e\) is its exact literal portal length. For a total order
\(\prec\) and a matching \(M\) of forward arcs, the exact fusion excess is

\[
 2H\bigl(|\mathcal E|-|M|\bigr)+\sum_{e\in M}\delta_e.
\tag{6.4}
\]

Equivalently, with weights \(w_e=2H-\delta_e\), the optimum is

\[
 \boxed{
 2H|\mathcal E|-\max_\prec\nu_w(D_\prec),}
\tag{6.5}
\]

where \(\nu_w\) is maximum matching weight. This is the exact multiepoch
version of the local portal saving. The empty matching is allowed. Every
portal arc used here must terminate in the exact decorated initial useful
state from which the target epoch's internal rotor path continues; center
adjacency or rankwise compatibility is insufficient.

If \(\mathcal H_0\) is the family of desired band masks absent from the
marked epoch flags and \(G(M)\) counts members of \(\mathcal H_0\)
represented at the nonmarked initialization and portal positions, literal
completion has exact declared length

\[
 T+2H(|\mathcal E|-|M|)
 +\sum_{e\in M}\delta_e
 +|\mathcal H_0|-G(M).
\tag{6.6}
\]

For a single new fusion arc, let
\(g=G_{\rm new}-G_{\rm old}\) be the signed net change in declared raw
support. The exact change in this ledger is

\[
 \boxed{\delta_e-2H-g.}
\tag{6.7}
\]

This is the requested no-isolated-reset portal identity. It is exact for
the declared literal-completion policy. Incidental witnesses not counted
in \(G\) can only shorten the unrestricted optimum.

### Theorem 6.3 (conditional exact-ownership fusion)

Fix \(1\le H<m\). Suppose \(p\) decorated, constant-radius-\(H\),
\(B\)-center rotor epochs have the following properties.

1. Their common marked flags cover every mask in every rank
   \(m-H,\ldots,m+H\).
2. Their total number of center occurrences is

   \[
   T=pB=W+D_0.
   \tag{6.8}
   \]

   Full middle coverage implies \(D_0\ge0\).

3. The endpoint digraph built from these same decorated representatives
   has

   \[
   J_0=\operatorname{pc}(D).
   \tag{6.9}
   \]

Then, after retaining one occurrence of each middle mask, there is a
spanning rotor forest with \(W\) distinct middle owners and at most

\[
 C\le J_0+D_0
\tag{6.10}
\]

components. Literal repair gives

\[
 \boxed{
 \mathcal L_{\rm band}
 \le W+2HJ_0+4HD_0.}
\tag{6.11}
\]

In addition, it contains a set of \(e\) forest edges whose lower and upper
first-band colors are separately rainbow, with

\[
 \boxed{
 N_1-e\le
 (W-N_1)+2D_0+C
 \le\frac{W}{m+1}+J_0+3D_0.}
\tag{6.12}
\]

Therefore

\[
 J_0=o(W/H),\qquad D_0=o(W/H)
\tag{6.13}
\]

suffice for both a \(W+o(W)\) literal band word and an exact spanning rotor
forest with an asymptotically complete certified edge set whose two
first-band color families are separately rainbow.

#### Proof

Choose a \(J_0\)-path cover of the epochs. Formula (6.1) gives the
untrimmed word length

\[
 T+2HJ_0=W+D_0+2HJ_0.
\tag{6.14}
\]

Delete all but one occurrence of every middle mask. Deleting \(D_0\)
vertices from \(J_0\) paths leaves at most \(J_0+D_0\) nonempty contiguous
path components, proving (6.10). Reinitializing them costs \(2HC\) beyond
the \(W\) marked centers. A deleted center carried one target at each of
the \(2H\) signed nonmiddle depths, so at most \(2HD_0\) distinct targets
lose their last witness. Appending those targets gives

\[
 W+2HC+2HD_0
 \le W+2HJ_0+4HD_0.
\]

For (6.12), after deletion the support of the lower depth-one vertex flags
and of the upper depth-one vertex flags is at least \(N_1-D_0\) on each
side. Removing the \(C\) terminal lower flags and the \(C\) initial upper
flags leaves edge-color supports

\[
 a_-,a_+\ge N_1-D_0-C.
\tag{6.15}
\]

Make a bipartite multigraph whose left vertices are realized lower colors,
whose right vertices are realized upper colors, and whose \(W-C\) edges
are the forest edges. If it has \(c_{\rm col}\) connected components, then

\[
 W-C\ge a_-+a_+-c_{\rm col}.
\tag{6.16}
\]

Choosing one multigraph edge from each component gives \(c_{\rm col}\)
forest edges with both color coordinates distinct. Hence

\[
 e\ge c_{\rm col}
 \ge2N_1-W-2D_0-C,
\]

which is (6.12). \(\square\)

Every adjective in Theorem 6.3 is essential:

- the objects are decorated epochs, not Boolean supports;
- the cover, orientations, flags, and endpoint path cover are one common
  choice;
- the epochs have genuine constant radius \(H\);
- a generic economical cover with only \(D_0=o(W)\) is insufficient for
  trimming; the stronger \(D_0=o(W/H)\) is needed;
- recomputing future queues after joining bare epochs changes an
  \(H\)-step suffix of the preceding decoration and therefore does not
  prove the theorem's hypotheses.

---

## 7. Sharp ceiling for recoalesced states

The refined tail in Theorems 2.1 and 5.1 is forced by the following
obstruction.

Call a complete state **minimal \(H\)-saturated** if it has the form

\[
 \Pi=(L,\{a_1\},\ldots,\{a_{2H}\},R),
 \qquad |L|=|R|=m-H.
\tag{7.1}
\]

It has the minimum possible \(2H+2\) blocks among states exposing every
rank \(m-H,\ldots,m+H\). Its middle and top flags are

\[
 S=L\cup\{a_1,\ldots,a_H\},
\qquad
 U=\Omega\setminus R.
\tag{7.2}
\]

Assume in this section that

\[
 1\le H\le m-2,
\tag{7.3}
\]

so both end blocks have size at least two.

### Theorem 7.1 (exact tight-state transition graph)

If one MTF update carries one minimal \(H\)-saturated state to another,
then it is exactly one of the following:

1. \(X=L\), which is idempotent; or
2. for \(b\in L\) and \(1\le j\le2H\),

   \[
   X=(L-\{b\})\cup\{a_j\},
   \tag{7.4}
   \]

   with target

   \[
   \bigl(
   L-b+a_j,\{b\},
   \{a_1\},\ldots,\widehat{\{a_j\}},\ldots,
   \{a_{2H}\},R
   \bigr).
   \tag{7.5}
   \]

In particular, the residual \(R\), and therefore the top flag \(U\), is
frozen. There are exactly

\[
 2H(m-H)
\tag{7.6}
\]

nontrivial tight successors.

#### Proof

The source and target both have \(2H+2\) blocks. Lemma 1.2 says that
exactly one source block is swallowed by \(X\). The target first block has
size \(m-H\).

If \(R\) is swallowed, then \(X=R\); the next surviving block is \(L\), of
size at least two, contradicting the singleton second block in (7.1). If
\(L\) is swallowed, cardinality forces \(X=L\), giving the idempotent
case.

Otherwise the swallowed block is one singleton \(\{a_j\}\). The first
surviving source block \(L\setminus X\) must be the singleton second target
block. Since \(|X|=|L|\), this forces

\[
 L\setminus X=\{b\},\qquad X=(L-\{b\})\cup\{a_j\}.
\]

Direct subtraction gives (7.5). The count in (7.6) is immediate.
\(\square\)

If \(j\le H\), the middle owner is unchanged. If \(j>H\), its projected
move removes \(a_H\) and adds \(a_j\). Thus there is ample Johnson mobility
inside one frozen top fibre; only movement between fibres is obstructed.

### Theorem 7.2 (sharp cross-fibre portal distance)

Let \(\Pi,\Pi'\) be minimal \(H\)-saturated states with residuals
\(R\ne R'\). Any MTF word carrying \(\Pi\) to \(\Pi'\) has length at least

\[
 \boxed{2H+1.}
\tag{7.7}
\]

The bound is attained for some pairs. Hence the exact minimum cross-fibre
excess over one transition is \(2H\).

#### Proof

Suppose first that some coordinate of \(R'\) is touched during the bridge.
Because \(R'\) is one final block, all of it must receive one common final
touch time. The other \(2H+1\) target blocks precede it and need distinct
later last-occurrence times. Thus at least \(2H+2\) updates are required.

Suppose instead that \(R'\) is untouched. All its elements must lie in one
source block, because untouched source blocks have distinct old timestamps.
Since \(|R'|=m-H\ge2\), cardinality forces \(R'=L\) or \(R'=R\). The
second is excluded. Thus \(R'=L\).

The source block \(L\) is initially newest and must finish oldest. Every
one of the other \(2H+1\) target blocks must therefore receive a distinct
new timestamp, proving (7.7).

For sharpness, take \(R'=L\), choose the other target blocks to partition
\(\Omega\setminus L\), and write those \(2H+1\) blocks once in reverse
target order. The untouched \(L\) becomes the target residual.
\(\square\)

### Theorem 7.3 (global top-support ceiling)

Let \(A_1,\ldots,A_{\mathcal L}\) be any nonzero OR word. Let \(E\) be the
number of positions whose complete state is not minimal \(H\)-saturated.
Then

\[
 \boxed{
 |\mathcal R_{m+H}(A)|
 \le E+\left\lfloor\frac{E}{2H}\right\rfloor+1.}
\tag{7.8}
\]

Equivalently, if \(M_H^+\) is the top-rank defect,

\[
 \boxed{
 M_H^++E+\left\lfloor\frac{E}{2H}\right\rfloor
 \ge N_H-1.}
\tag{7.9}
\]

Full top-rank coverage therefore forces

\[
 \boxed{
 E\ge
 \left\lceil\frac{2H}{2H+1}(N_H-1)\right\rceil.}
\tag{7.10}
\]

#### Proof

At any nonminimal endpoint, Lemma 1.1 allows at most one represented
rank-\(m+H\) set, contributing at most \(E\) in total.

At a minimal endpoint, the unique top prefix is \(\Omega\setminus R\).
Between consecutive minimal endpoints with different residuals, Theorem
7.2 requires at least \(2H+1\) bridge letters, hence at least \(2H\)
strictly intervening nonminimal endpoints. These gaps are disjoint. The
minimal endpoints therefore display at most

\[
 \left\lfloor E/(2H)\right\rfloor+1
\]

distinct top flags. This proves (7.8), and the remaining assertions follow
by rearrangement. \(\square\)

### Corollary 7.4 (recanonicalization cannot have coefficient one)

If the word covers the full rank \(m+H\) and every middle mask is witnessed
at a minimal \(H\)-saturated endpoint, then

\[
 \boxed{
 \mathcal L\ge
 W+\left\lceil\frac{2H}{2H+1}(N_H-1)\right\rceil.}
\tag{7.11}
\]

In particular:

- if \(H\to\infty\) and \(H=o(\sqrt m)\), then

  \[
  \mathcal L\ge(2-o(1))W;
  \tag{7.12}
  \]

- if \(H=t\sqrt m+o(\sqrt m)\), for fixed \(t>0\), then

  \[
  \mathcal L\ge(1+e^{-t^2}-o(1))W.
  \tag{7.13}
  \]

#### Proof

By Lemma 1.1, the \(W\) distinct middle masks require \(W\) distinct
minimal endpoints. Hence \(\mathcal L-W\ge E\), and (7.11) follows from
(7.10).

Finally,

\[
 \frac{N_H}{W}
 =\prod_{i=0}^{H-1}\frac{m-i}{m+i+1}
 =\exp\!\left(-\frac{H^2}{m}+o(1)\right)
\tag{7.14}
\]

in the two stated regimes. Substitute this into (7.11). \(\square\)

The constant in (7.7)--(7.10) is locally sharp: a residual change can cost
exactly \(2H+1\) letters. The theorem does not claim that one global word
simultaneously attains a new top mask at every intervening endpoint.

More generally, any \(W+o(W)\) band word with full top-rank coverage has

\[
 E\ge\left(\frac{2H}{2H+1}+o(1)\right)N_H.
\tag{7.15}
\]

Thus, when \(H\to\infty\), \(H=o(\sqrt m)\), almost every useful position
must be nonminimal. If it remains radius-\(H\) saturated, it must carry
extra old blocks; in the refined-cylinder normal form these are stale tail
blocks. The refined cylinders of Sections 2, 5, and 6 are exactly this
necessary escape.

---

## 8. A short-epoch obstruction

The priority portals do not rescue cyclic interval epochs whose half-length
\(\ell\) is at most the radius \(H\). Consider a cut \(2\ell\)-center
moving-interval strip. After the cut, continue with the \(\ell\) cyclic
moving-coordinate dummy departures in their cyclic order, and only then
use \(H-\ell\) fixed dummy core exits.

### Proposition 8.1

If \(\ell\le H\), every one of the \(2\ell-1\) internal arrivals has target
priority \(j=\ell-1\). Hence

\[
 \boxed{
 J_{\rm strip}=(2\ell-1)(H-\ell+1).}
\tag{8.1}
\]

For every \(q\ge\ell\), the lower \(q\)-flag is constant along the strip
(up to the fixed dummy-core deletion). In particular, a family of such
strips with \(p\) components supplies at most \(p\) deepest lower labels
among its marked cylinder flags.

#### Proof

Every arriving moving coordinate leaves exactly \(\ell\) transitions
later. The strip is FIFO: every coordinate arriving later also leaves
later. Hence exactly the other \(\ell-1\) moving coordinates present at
entry have first exits before it. Thus \(j=\ell-1\), and Theorem 2.1 gives
excess \(H-\ell+1\) at each internal transition. This proves (8.1).

At lower depth \(q\ge\ell\), all \(\ell\) moving coordinates have been
removed by the future-departure prefix. What remains is the fixed core with
the same first \(q-\ell\) dummy-core coordinates removed, independent of
the strip position. \(\square\)

Thus even \(\ell=H\) costs essentially one extra letter per marked center
and supplies only one deepest lower mask per component. Shortening cyclic
epochs below the queue radius is a genuine dead end for a backbone built
from these epochs. Indeed, if \(T=2\ell p\ge W\) middle occurrences are
carried, then

\[
 J_{\rm strip}
 =p(2\ell-1)(H-\ell+1)
 \ge \frac{T}{2}\ge\frac W2.
\tag{8.2}
\]

Incidental portal witnesses cannot remove this linear raw toll. Fresh rotor
epochs evade the obstruction because their arrivals enter the lower core
rather than returning inside the queue horizon.

---

## 9. Exact remaining lemmas

### 9.1 Global-priority form

For a depth function \(H=H(m)\), the smallest sufficient statement exposed
by Theorem 4.4 is the following.

> **Common decorated cylinder assembly \(\mathrm{CDCA}_H\) — UNPROVED.**
> There is one oriented Johnson forest of compatible refined cylinders
> covering every middle mask, with
> \[
> D_0=o(W/H),\qquad C=o(W/H),
> \tag{9.1}
> \]
> and
> \[
> \sum_{q=1}^H(M_q^-+M_q^+)=o(W).
> \tag{9.2}
> \]
> The lower and upper flags in (9.2) belong to the same cylinders and the
> same middle owners.

For

\[
 H=o(m^{1/3}),
\tag{9.3}
\]

\(\mathrm{CDCA}_H\) immediately implies a literal
\(W+o(W)\) band word by Theorem 4.4. This conditional dynamical range is
far beyond the former
\(o(\sqrt{\log m/\log\log m})\) reset scale.

At Gaussian depth \(H=\lceil A\sqrt m\rceil\), (9.1)--(9.2) alone do not
control (4.24). The precise replacement is

> **Gaussian common decorated cylinder assembly
> \(\mathrm{GCDCA}_A\) — UNPROVED.**
> For fixed \(A\), there is one common cylinder forest satisfying
> (9.1)--(9.2) and
> \[
> J=o(W).
> \tag{9.4}
> \]

By the exact equality (4.9), condition (9.4) is equivalently the
leading-order projected cycle/merge balance

\[
 \sum_{q=1}^H(\beta_q+\mu_q)
 =
 HD_0+\sum_{q=1}^H(W-N_q+M_q^-)+o(W).
\tag{9.5}
\]

This is strictly more informative than a separate short-run count.

Neither \(\mathrm{CDCA}_H\) nor \(\mathrm{GCDCA}_A\) follows from a
different matching at every depth. Both demand one integral, nested,
common-ownership chronology.

### 9.2 Predecorated epoch form

For the economical-epoch implementation, a more local sufficient statement
is:

> **Correlated rotor endpoint lemma \(\mathrm{CRE}_H\) — UNPROVED.**
> Select one family of decorated constant-radius-\(H\), \(B\)-center rotor
> epochs which covers the band and satisfies
> \[
> D_0=o(W/H),\qquad
> \operatorname{pc}(D)=o(W/H),
> \tag{9.6}
> \]
> where \(D\) is built from those very same annotated endpoints.

Theorem 6.3 proves that \(\mathrm{CRE}_H\) is sufficient, with every seam
and every deletion loss explicitly charged.

If a decorated constant-radius epoch cover satisfies the analogue of the
audited augmented-cover estimate, its exponent has the form

\[
 \eta=
 \left(
 O\!\left(\frac{B\log m}{m}\right)
 \right)^{1/(B(2H+1)-1)}.
\tag{9.7}
\]

To obtain \(D_0=O(\eta W)=o(W/H)\), it is enough that

\[
 BH\log H=o(\log m).
\tag{9.8}
\]

If the correlated endpoint part of \(\mathrm{CRE}_H\) could be proved
without requiring \(B/H\to\infty\), a slowly chosen \(B\) would permit

\[
 H=o\!\left(\frac{\log m}{\log\log m}\right).
\tag{9.9}
\]

This is a doubly conditional depth improvement, not an unconditional
theorem: the audited exponent belongs to the augmented
dummy/variable-profile cover and does not itself prove its constant-radius
analogue; even such a constant-radius cover would not generically control
its endpoint path cover.

Independent epoch rounding retains the old ceiling. More precisely, under
the audited probabilistic architecture in which annotations are
conditionally independent across \(B\)-center blocks and
\(R_H=(1+o(1))W\), with probability tending to one,

\[
 \operatorname{pc}(D)\ge(1-o(1))\frac{W}{B}.
\tag{9.10}
\]

Then vanishing endpoint toll requires \(B/H\to\infty\). Combined with
(9.8), this gives

\[
 H^2\log H=o(\log m),
\qquad
 H=o\!\left(\sqrt{\frac{\log m}{\log\log m}}\right).
\tag{9.11}
\]

Thus any improvement through (9.9) must use leading-order correlated
endpoint ownership. Independent epochs cannot provide it.

---

## 10. Adversarial audit

The main claims were checked independently against the following failure
modes.

1. **Priority sharpness.** The lower bound \(H-j+1\) is only for the
   prescribed chronological lower prefix. It is false for an arbitrary
   saturated state over the same target middle set.
2. **Endogenous upper flags.** A portal inherits its target upper queue
   from the source. Joining bare middle paths and recomputing priorities can
   destroy previously selected deep upper flags.
3. **Tail scope.** The rotor graph is closed only on abstract prefixes.
   A closed abstract tour need not return the complete physical
   last-occurrence state; stale tail blocks generally accumulate.
4. **Projection identity.** The defects \(M_q^\pm\) in (4.8)--(4.15) count
   marked-cylinder flags only. Incidental portal witnesses cannot be
   inserted into the projected Euler identity. They may only be credited
   through \(G\) in (4.20).
5. **Initialization constant.** A useful refined prefix takes \(2H+1\)
   writes, but its last write is already the first marked center. The
   excess is \(2H\), as used throughout.
6. **Run-length warning.** Priority is the first-exit rank among
   contemporaries, not elapsed return length. Theorem 3.2 is exact only
   with the corrected active intervals and weights \(H-j_R\), together
   with the zero-toll terminal completion of Lemma 2.4.
7. **The \(m^{1/3}\) threshold.** This comes only from discarding the
   nonnegative cycle/merge term in (4.9). It is not an architecture
   ceiling. At Gaussian depth the exact cancellation (9.5), not (4.12), is
   the relevant target.
8. **Tight-state ceiling.** Theorems 7.1--7.3 allow arbitrary bridge
   letters and count incidental top witnesses, but they apply only when the
   marked states are minimal. Refined stale-tail cylinders deliberately lie
   outside that class.
9. **Epoch ownership.** Theorem 6.3 requires one decorated cover and one
   endpoint path cover. Rankwise endpoint matchings, undecorated center
   adjacency, or fractional flow do not instantiate it.
10. **Exact factor status.** No exact wreath factor satisfying the
    fixed-window balanced nested quotas is constructed here. Therefore this
    report does not establish the fixed-window MWB reduction and does not
    prove the contiguous-OR conjecture.

---

## 11. Final status

The route is genuinely advanced but incomplete.

- The new hybrid priority state graph eliminates isolated resets and gives
  sharp local portal costs, the exact priority-cut identity
  (3.4)--(3.5), and the exact weighted epoch ledger (6.4)--(6.7).
- The exact loop identity (4.9) shows that, up to \(o(m^{1/3})\) depth,
  seam cost is automatically absorbed by common lower support.
- The refined rotor graph gives a concrete exact endpoint path-cover target
  and a fully audited trimming/first-band theorem.
- The minimal-state support ceiling proves that any attempt to obtain this
  fusion by repeatedly recoalescing the tail loses coefficient one, with
  the sharp local constant \(2H\).

The smallest surviving obstruction is common decorated assembly:
\(\mathrm{CDCA}_H\) for mesoscopic depth, or its endpoint form
\(\mathrm{CRE}_H\). At fixed Gaussian windows the stronger exact
cycle-surplus condition \(\mathrm{GCDCA}_A\) is necessary. These lemmas are
unproved.

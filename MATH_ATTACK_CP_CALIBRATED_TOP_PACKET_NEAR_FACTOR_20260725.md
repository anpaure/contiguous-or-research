# The calibrated top-packet reduction

Date: 2026-07-25

Pure mathematics only.  This note uses no computation, search, or
unproved reduction from arbitrary near-optimal OR words.  Every packet below
is a literal bridge-one promotion cycle, and every claimed lower or upper
mask is an actual flag of one of its states.

## 0. Outcome

Put

\[
 W=\binom{2m}{m},\qquad N_h=\binom{2m}{m-h},\qquad
 \lambda_h=\frac{W}{N_h}.
\]

Choose the least positive integer \(H\) such that

\[
 \lambda_H\ge m+H,
 \qquad M:=m+H,
 \qquad r:=m-H=2m-M.
\tag{0.1}
\]

The following facts are proved here.

1. The calibration is sharp:
   \[
   H\sim\sqrt{m\log m},\qquad
   1\le\frac{\lambda_H}{M}=1+o(1).
   \tag{0.2}
   \]
   Consequently
   \[
   MN_H=W-o(W),\qquad HN_H=o(W).
   \tag{0.3}
   \]
   In fact
   \[
   0\le W-MN_H<\frac{2(H-1)}{M-1}W,
   \qquad
   HN_H\le\frac HM W.
   \tag{0.4}
   \]

2. Every cyclic order on a top \(U\in\binom{[2m]}M\) gives a genuine
   promotion cycle of length \(M\).  Its middle owners are the \(M\)
   cyclic \(m\)-intervals, and its flags at every rank
   \(m-H,\ldots,m+H\) are exactly the cyclic intervals of that rank.

3. The scalar integral capacity problem has no obstruction.  If the
   requirement that the \(M\) owners at one top form one cyclic packet is
   deleted, a capacitated Hall matching assigns \(M\) distinct middle
   owners to every top, with no owner assigned twice.

4. The top-tagged middle-packet hypergraph has exact degree and codegree
   formulae.  In particular, for two middle owners at Johnson distance
   \(t\),
   \[
   \frac{\operatorname{codeg}(X,Y)}{d_m}
   =\begin{cases}
   2\binom mt^{-2},&1\le t<H,\\[1mm]
   (m-H+1)\binom mH^{-2},&t=H,\\[1mm]
   0,&t>H.
   \end{cases}
   \tag{0.5}
   \]
   Hence its maximum relative middle codegree is exactly \(2/m^2\) for
   all sufficiently large \(m\).

5. There is an exact augmented packet hypergraph which incorporates all
   band ranks without violating their different capacities.  At rank \(k\)
   a packet claims
   \[
   s_k:=\min\left\{M,
       \left\lfloor\frac{\binom{2m}{k}}{N_H}\right\rfloor\right\}
   \tag{0.6}
   \]
   of its \(M\) interval flags.  The completely symmetric weights give a
   fractional matching which saturates every top tag and has load at most
   one on every claimed mask.  Its total fractional defect is exactly the
   audited floor deficit.

6. An integral matching in this augmented hypergraph which saturates all
   top tags would prove the desired top-packet construction, with
   \(o(W)\) aggregate band holes, not merely \(o(W)\) holes separately at
   each rank.  Together with the promotion paths, the outer-rank tail and
   reset toll are also \(o(W)\), so this matching lemma gives a
   coefficient-one construction.

The integral matching lemma is not proved here.  The calculations identify
why neither independent rounding nor a routine one-stage nibble completes
it:

* independent uniform packet choices leave
  \((e^{-1}+o(1))W\) middle owners uncovered in expectation;
* the augmented edge size is
  \[
  (\sqrt\pi+o(1))m^{3/2};
  \]
* adjacent nested ranks have normalized codegree \(\Theta(1/m)\).

Thus the all-rank augmented object is not locally sparse at its own edge
scale.  This is a sharp obstruction to the naive rounding argument, not a
refutation of the top-packet construction.  The exact remaining assertion
is the tag-saturating augmented packet matching stated in Section 8.

## 1. Calibration of the depth

The exact factorial form is

\[
 \lambda_h
 =\frac{(m-h)!(m+h)!}{(m!)^2}
 =\prod_{i=1}^{h}\frac{m+i}{m-i+1}.
\tag{1.1}
\]

For \(h=o(m^{2/3})\), Taylor expansion, uniformly over the summands in
(1.1), gives

\[
 \log\lambda_h
 =\frac{h^2}{m}
   +O\left(\frac hm+\frac{h^3}{m^2}\right).
\tag{1.2}
\]

Indeed,

\[
 \log\frac{m+i}{m-i+1}
 =\frac{2i-1}{m}+O\left(\frac1{m^2}+\frac{i^2}{m^2}\right),
\]

and summing gives (1.2).  The slightly weaker error displayed there is
more than sufficient in the range used below.

### Proposition 1.1 (location of the first crossing)

The least \(H\) satisfying (0.1) obeys

\[
 \boxed{H\sim\sqrt{m\log m}.}
\tag{1.3}
\]

#### Proof

Fix \(\varepsilon>0\), and put

\[
 h_\pm=(1\pm\varepsilon)\sqrt{m\log m}.
\]

Both are \(o(m^{2/3})\).  Equation (1.2) gives

\[
 \log\lambda_{h_\pm}
 =(1\pm\varepsilon)^2\log m+o(\log m).
\]

For large \(m\), the lower value is smaller than \(\log(m+h_-)\), while
the upper value is larger than \(\log(m+h_+)\).  Hence the first crossing
lies between \(h_-\) and \(h_+\).  Letting \(\varepsilon\downarrow0\)
proves (1.3).  \(\square\)

### Proposition 1.2 (minimality removes the overshoot)

For the least \(H\),

\[
 \boxed{
 1\le\frac{\lambda_H}{M}
 <\frac{M-1}{m-H+1}
 =1+O\left(\frac Hm\right).}
\tag{1.4}
\]

Consequently \(\lambda_H/M=1+o(1)\), and (0.3)--(0.4) hold.

#### Proof

Minimality says \(\lambda_{H-1}<m+H-1=M-1\), while (1.1) gives

\[
 \frac{\lambda_H}{\lambda_{H-1}}
 =\frac{m+H}{m-H+1}=\frac{M}{m-H+1}.
\]

This proves the strict upper bound in (1.4); the lower bound is the
definition of \(H\).  Since \(H=o(m)\), the ratio tends to one.

Now

\[
 \frac{MN_H}{W}=\frac{M}{\lambda_H}.
\]

The upper bound in (1.4) therefore implies

\[
 \frac{MN_H}{W}>
 \frac{m-H+1}{M-1},
\]

and hence

\[
 0\le\frac{W-MN_H}{W}
 <1-\frac{m-H+1}{M-1}
 =\frac{2(H-1)}{M-1}.
\]

Finally,

\[
 \frac{HN_H}{W}=\frac{H}{\lambda_H}\le\frac HM=o(1).
\]

This proves all assertions.  \(\square\)

The choice of the *least* crossing is important.  Merely knowing
\(H\asymp\sqrt{m\log m}\) would give \(N_H=\Theta(W/m)\), but would not
give the near-equality \(MN_H=W-o(W)\) with the exact one-sided capacity
needed below.

## 2. One cyclic top packet is a literal promotion cycle

Fix a top

\[
 U\in\binom{[2m]}M
\]

and an oriented cyclic order

\[
 C=(a_i:i\in\mathbb Z_M)
\]

of its elements.  Recall \(r=m-H\), so

\[
 M=r+2H.
\tag{2.1}
\]

For every \(i\in\mathbb Z_M\), define the full radius-\(H\) state

\[
 \omega_i=(L_i;z_{i,1},\ldots,z_{i,2H};R),
 \qquad R=[2m]\setminus U,
\tag{2.2}
\]

by

\[
 L_i=\{a_i,a_{i+1},\ldots,a_{i+r-1}\},
 \qquad z_{i,j}=a_{i-j}.
\tag{2.3}
\]

The indices in (2.3) partition the cyclic order because of (2.1).

### Proposition 2.1 (last-singleton promotion)

For every \(i\), \(\omega_i\to\omega_{i+1}\) is a bridge-one promotion.
Thus \((\omega_i:i\in\mathbb Z_M)\) is a promotion cycle of length \(M\)
inside the fixed top fibre \(U\).

#### Proof

Use the promotion move with

\[
 x=a_i\in L_i,
 \qquad j=2H.
\]

Since \(M=r+2H\),

\[
 z_{i,2H}=a_{i-2H}=a_{i+r}.
\]

The new lower block is therefore

\[
 L_i-a_i+a_{i+r}=L_{i+1},
\]

while the new singleton list is

\[
 (a_i,a_{i-1},\ldots,a_{i-2H+1})
 =(z_{i+1,1},\ldots,z_{i+1,2H}).
\]

The residual block is unchanged.  This is exactly \(\omega_{i+1}\).
\(\square\)

### Proposition 2.2 (simultaneous interval flags)

The middle owner of \(\omega_i\) is the cyclic \(m\)-interval

\[
 X_i=\{a_{i-H},a_{i-H+1},\ldots,a_{i+r-1}\}.
\tag{2.4}
\]

For \(0\le q\le H\), its lower and upper flags are

\[
 D_{i,q}
 =\{a_{i-H+q},\ldots,a_{i+r-1}\}
 \in\binom U{m-q},
\tag{2.5}
\]

\[
 A_{i,q}
 =\{a_{i-H-q},\ldots,a_{i+r-1}\}
 \in\binom U{m+q}.
\tag{2.6}
\]

Consequently the packet exposes all \(M\) cyclic intervals at every rank
\(r\le k<M\), and it exposes its top \(U\) at rank \(M\).

#### Proof

The owner is \(L_i\) together with \(z_{i,1},\ldots,z_{i,H}\), which gives
(2.4).  The depth-\(q\) lower flag uses the first \(H-q\) singletons and
the upper flag the first \(H+q\); this gives (2.5)--(2.6).  For
\(0<k<M\), the \(M\) cyclic \(k\)-intervals are distinct.  At \(k=M\)
they all equal \(U\).  \(\square\)

This is an explicit flag exposure.  No converse assertion about general OR
words or singleton near-Ucycles is being used.

## 3. The top-tag quotient and the unrestricted Hall theorem

It is useful to write a top by its omitted tag

\[
 R=[2m]\setminus U\in\binom{[2m]}r.
\]

If \(X\subset U\) is a middle owner, put \(Y=[2m]\setminus X\).  Then

\[
 R\subset Y,qquad |Y|=m,
\tag{3.1}
\]

and

\[
 Y=R\mathbin{\dot\cup}(U\setminus X).
\tag{3.2}
\]

For a cyclic packet, the \(H\)-sets \(U\setminus X\) in (3.2) are exactly
the \(M\) cyclic \(H\)-intervals of its order.  Thus the packet condition is
a bundle condition inside the ordinary inclusion graph

\[
 \binom{[2m]}r\longleftrightarrow\binom{[2m]}m,
 \qquad R\sim Y\iff R\subset Y.
\tag{3.3}
\]

### Proposition 3.1 (unrestricted integral capacity)

If the cyclic-bundle condition is deleted, there is an integral assignment
of \(M\) distinct neighbours \(Y\) to every tag \(R\), with no middle
\(Y\) assigned to two tags.

#### Proof

The left and right degrees in (3.3) are

\[
 a=\binom MH,
 \qquad b=\binom mH.
\tag{3.4}
\]

Double counting gives

\[
 N_Ha=Wb,
 \qquad \frac ab=\lambda_H\ge M.
\tag{3.5}
\]

For a family \(\mathcal R\) of tags, all \(a|\mathcal R|\) incident edges
land in its neighbourhood, and every right vertex receives at most \(b\)
of them.  Hence

\[
 |N(\mathcal R)|\ge\frac ab|\mathcal R|
 \ge M|\mathcal R|.
\tag{3.6}
\]

Replace every tag by \(M\) identical demand copies.  Equation (3.6) is
Hall's condition, and a matching saturating all copies gives the required
assignment.  \(\square\)

Thus divisibility, total capacity, and top ownership are not the issue.  The
remaining middle problem is precisely whether every group of \(M\) assigned
neighbours can be required to be the cyclic \(H\)-interval bundle of one
order.

## 4. The top-tagged middle-packet hypergraph

Use oriented cyclic orders modulo rotation.  There are

\[
 (M-1)!
\tag{4.1}
\]

such orders on a fixed top \(U\).  Reversal gives the same unordered
families of interval masks, but it gives the opposite directed promotion
cycle.  Keeping both orientations only introduces a uniform multiplicity
two and makes the counts cleaner.

Define \(\mathcal P_m\) as follows.

* Its first vertex class is the set of top tags
  \(U\in\binom{[2m]}M\).
* Its second vertex class is the middle layer
  \(X\in\binom{[2m]}m\).
* An edge indexed by \((U,C)\) contains the tag \(U\) and the \(M\)
  cyclic \(m\)-intervals of \(C\).

An edge matching which saturates all tags is exactly one packet per top with
pairwise disjoint middle packets.

### Proposition 4.1 (degrees at every rank)

More generally, fix \(r\le k<M\).  The number of indexed packets in which
a fixed rank-\(k\) mask \(S\) occurs as a cyclic interval is

\[
 \boxed{
 d_k=\binom{2m-k}{M-k}k!(M-k)!
     =\frac{k!(2m-k)!}{r!}.}
\tag{4.2}
\]

The tag degree is

\[
 d_{\rm tag}=(M-1)!,
\tag{4.3}
\]

and

\[
 \boxed{
 \frac{d_k}{d_{\rm tag}}
 =\frac{MN_H}{\binom{2m}{k}}.}
\tag{4.4}
\]

In particular,

\[
 d_m=\binom mH m!H!=\frac{(m!)^2}{r!},
 \qquad
 \frac{d_m}{d_{\rm tag}}=\frac{M}{\lambda_H}=1-o(1).
\tag{4.5}
\]

#### Proof

There are \(\binom{2m-k}{M-k}\) tops containing \(S\).  In one such top,
the number of oriented cyclic orders in which \(S\) is an interval is

\[
 k!(M-k)!.
\]

This follows either by contracting \(S\) and its complementary interval to
two ordered blocks, or by double counting a marked interval start.  This
proves (4.2).  Equations (4.3)--(4.5) are direct simplifications.  \(\square\)

### Proposition 4.2 (exact middle pair codegrees)

Let \(X,Y\) be distinct middle masks and

\[
 t=|X\setminus Y|=|Y\setminus X|.
\]

Their packet codegree is zero for \(t>H\).  For \(1\le t<H\),

\[
 \operatorname{codeg}(X,Y)
 =\binom{m-t}{H-t}
   2(t!)^2(H-t)!(m-t)!,
\tag{4.6}
\]

while for \(t=H\),

\[
 \operatorname{codeg}(X,Y)
 =(H!)^2(r+1)!.
\tag{4.7}
\]

Dividing by \(d_m\) gives (0.5).

#### Proof

A common top must contain \(X\cup Y\), whose size is \(m+t\).  Therefore
there are \(\binom{m-t}{H-t}\) common tops if \(t\le H\), and none if
\(t>H\).

Fix a common top and put

\[
 A=U\setminus X,qquad B=U\setminus Y.
\]

Both are \(H\)-intervals in a containing cyclic order.  If \(t<H\), their
four membership blocks have sizes

\[
 |A\setminus B|=t,quad |A\cap B|=H-t,quad
 |B\setminus A|=t,quad |U\setminus(A\cup B)|=m-t.
\]

There are two possible cyclic orders of these four blocks, and arbitrary
orders inside them.  This gives

\[
 2(t!)^2(H-t)!(m-t)!
\]

orders per common top and proves (4.6).

If \(t=H\), the two \(H\)-intervals are disjoint.  Contracting them to two
labeled blocks leaves \(r\) labeled singleton elements on the circle.
There are \((r+1)!\) cyclic orders of these \(r+2\) objects and \((H!)^2\)
internal orders, proving (4.7).

Finally, for \(t<H\), substitution into (4.6) gives

\[
 \frac{\operatorname{codeg}(X,Y)}{d_m}
 =2\left(\frac{t!(m-t)!}{m!}\right)^2
 =\frac{2}{\binom mt^2}.
\]

For \(t=H\), (4.7) gives

\[
 \frac{\operatorname{codeg}(X,Y)}{d_m}
 =(r+1)\left(\frac{H!r!}{m!}\right)^2
 =\frac{r+1}{\binom mH^2}.
\]

This proves the proposition.  \(\square\)

The other two pair types are also transparent.  Two distinct tags have
codegree zero.  If \(X\subset U\), then

\[
 \operatorname{codeg}(U,X)=m!H!,
\tag{4.8}
\]

so

\[
 \frac{\operatorname{codeg}(U,X)}{d_m}
 =\binom mH^{-1},
 \qquad
 \frac{\operatorname{codeg}(U,X)}{d_{\rm tag}}
 =\frac{M}{\binom Mm}.
\tag{4.9}
\]

The top tag therefore does not introduce a large pair codegree.

## 5. Why the band needs claimed slots

Selecting one packet per top produces \(MN_H\) interval occurrences at
every proper rank in the band.  These cannot all be treated as conflict
vertices.  At a rank \(k\) with

\[
 \binom{2m}{k}<MN_H,
\]

some repetitions are forced.  Conversely, coverage does not require every
one of the \(M\) occurrences to be reserved as a distinct resource.

The correct capacity-respecting decoration is (0.6).  For every
\(r\le k<M\), a decorated packet chooses a set

\[
 J_k\subseteq\mathbb Z_M,qquad |J_k|=s_k,
\tag{5.1}
\]

and claims the \(s_k\) interval masks

\[
 \{I_C(i,k):i\in J_k\}.
\]

All unclaimed interval flags remain genuinely exposed by the packet; they
are simply not used as matching resources.  At the middle rank,

\[
 s_m=M
\tag{5.2}
\]

because \(W/N_H=\lambda_H\ge M\).  Thus middle-packet disjointness is still
enforced exactly.

Let \(\mathcal P^{\rm aug}\) be the hypergraph whose vertices are

* one copy of every top tag \(U\), and
* one rank-labeled copy of every mask at ranks \(r,\ldots,M-1\),

and whose edges are the decorated packets just described.

### Proposition 5.1 (exact fractional matching)

Put

\[
 \mathcal A=\prod_{k=r}^{M-1}\binom M{s_k}.
\tag{5.3}
\]

The augmented tag degree is

\[
 D_{\rm tag}=(M-1)!\mathcal A.
\tag{5.4}
\]

A fixed rank-\(k\) target has augmented degree

\[
 D_k=d_k\mathcal A\frac{s_k}{M},
\tag{5.5}
\]

and hence

\[
 \boxed{
 \frac{D_k}{D_{\rm tag}}
 =\frac{s_kN_H}{\binom{2m}{k}}\le1.}
\tag{5.6}
\]

Giving every augmented edge weight \(D_{\rm tag}^{-1}\) therefore
saturates every tag exactly and respects every mask capacity.  At rank
\(k\), its total fractional deficit is exactly

\[
 \boxed{
 h_k:=\binom{2m}{k}-s_kN_H.}
\tag{5.7}
\]

#### Proof

Equation (5.4) counts the base cyclic order and all independent choices in
(5.1).  If a base packet contains a fixed target, that target has one unique
interval start.  The proportion of \(s_k\)-subsets containing this start is
\(s_k/M\), which proves (5.5).  Substitute (4.4) to obtain (5.6).

The symmetric edge weights give tag load one and target load
\(s_kN_H/\binom{2m}{k}\).  Summing the missing load over all targets at
that rank gives (5.7).  \(\square\)

This is a fractional matching, not an integral construction.  The incidence
matrix is a genuine hypergraph incidence matrix, not a network matrix; no
total-unimodularity conclusion is available.

### Proposition 5.2 (all floor losses sum to \(o(W)\))

Across the entire band,

\[
 \boxed{
 \sum_{k=r}^{M-1}h_k=o(W).}
\tag{5.8}
\]

#### Proof

Write \(k=m\pm q\) and \(N_q=\binom{2m}{m-q}\).  If the minimum in (0.6)
does not cap at \(M\), then

\[
 0\le N_q-s_{m-q}N_H<N_H.
\tag{5.9}
\]

There are \(O(H)\) such ranks, and

\[
 HN_H=o(W)
\]

by Proposition 1.2.

It remains to audit the ranks at which \(s_{m-q}=M\).  Put

\[
 D_0=W-MN_H.
\]

At a capped rank,

\[
 h_{m-q}=N_q-MN_H=D_0-(W-N_q)\le D_0,
\tag{5.10}
\]

and capping implies \(N_q\ge MN_H\), or

\[
 \lambda_q=\frac W{N_q}\le\frac W{MN_H}
 =\frac{\lambda_H}{M}=1+O(H/m).
\tag{5.11}
\]

Uniformly for \(q\le H\), (1.2) and a matching elementary lower bound give

\[
 \log\lambda_q\ge c\frac{q^2}{m}
\tag{5.12}
\]

for an absolute \(c>0\) and all large \(m\).  Equations (5.11)--(5.12)
show that every capped \(q\) satisfies

\[
 q=O(\sqrt H).
\tag{5.13}
\]

There are therefore only \(O(\sqrt H)\) capped ranks on each side.  By
(0.4),

\[
 D_0=O(HW/m),
\]

so their total contribution is

\[
 O(\sqrt H D_0)
 =O\left(\frac{H^{3/2}}mW\right)
 =o(W),
\tag{5.14}
\]

because \(H\sim\sqrt{m\log m}\).  Adding (5.9) proves (5.8).
\(\square\)

The capped-rank audit is necessary.  Bounding every capped rank by
\(D_0\) and then multiplying by all \(H\) ranks would lose a factor and
would not prove (5.8).

### Proposition 5.3 (augmented edge size)

Let \(R_*\) be the number of vertices in one augmented edge.  Then

\[
 \boxed{R_*=(\sqrt\pi+o(1))M\sqrt m
       =(\sqrt\pi+o(1))m^{3/2}.}
\tag{5.15}
\]

#### Proof

The tag is used once, the middle rank contributes \(M\), every depth
\(1\le q<H\) occurs on both sides, the bottom rank contributes one claimed
slot, and the top is already the tag.  Hence

\[
 R_*=1+M+2\sum_{q=1}^{H-1}s_{m-q}+1.
\tag{5.16}
\]

Uniformly for \(q\le H\), (1.2) gives

\[
 \frac{N_q}{N_H}=\frac{\lambda_H}{\lambda_q}
 =(1+o(1))M e^{-q^2/m}.
\tag{5.17}
\]

The floors contribute only \(O(H)\), and the cap at \(M\) changes the
Riemann sum by lower order because \(\lambda_H/M=1+o(1)\).  Therefore

\[
 \sum_{q=0}^{H}s_{m-q}
 =\left(\frac{\sqrt\pi}{2}+o(1)\right)M\sqrt m.
\tag{5.18}
\]

Substitution in (5.16) proves (5.15).  \(\square\)

## 6. Cross-rank codegrees and the rounding barrier

The exact same-rank middle codegrees remain (0.5), because all \(M\)
middle intervals are claimed.  Cross-rank incidences are larger.

### Proposition 6.1 (adjacent nested codegree)

Let \(S\subset T\), with \(|S|=k\), \(|T|=k+1\), and
\(r\le k<M-1\).  The number of base packets in which both are cyclic
intervals is

\[
 J_k=\frac{2k!(2m-k-1)!}{r!}.
\tag{6.1}
\]

Their augmented codegree is

\[
 J_k\mathcal A\frac{s_k}{M}\frac{s_{k+1}}M.
\tag{6.2}
\]

Consequently

\[
 \frac{\operatorname{codeg}_{\rm aug}(S,T)}{D_k}
 =\frac{2}{2m-k}\frac{s_{k+1}}M,
\tag{6.3}
\]

\[
 \frac{\operatorname{codeg}_{\rm aug}(S,T)}{D_{k+1}}
 =\frac{2}{k+1}\frac{s_k}M.
\tag{6.4}
\]

Near the middle these quantities are \(\Theta(1/m)\).

#### Proof

Choose a top containing \(T\).  Conditional on \(T\) being an interval,
the set \(S=T\setminus\{x\}\) is also an interval exactly when \(x\) is
one of the two endpoints of the linear \((k+1)\)-block.  Thus the number
of orders per containing top is

\[
 2k!(M-k-1)!.
\]

There are \(\binom{2m-k-1}{M-k-1}\) containing tops, which simplifies to
(6.1).  The two claimed-start choices lie at different ranks and contribute
the independent factors in (6.2).  Dividing by (5.5), and using

\[
 \frac{J_k}{d_k}=\frac2{2m-k},
 \qquad
 \frac{J_k}{d_{k+1}}=\frac2{k+1},
\]

gives (6.3)--(6.4).  \(\square\)

Because \(R_*=\Theta(m^{3/2})\), the elementary local-sparsity product for
the augmented object is at least of order

\[
 R_*\cdot\Theta(1/m)=\Theta(\sqrt m),
\tag{6.5}
\]

not \(o(1)\).  Thus one cannot justify a growing-uniformity nibble by merely
substituting the pair-codegree ratios into a fixed-uniformity theorem.  The
nested incidences must be quotiented, exposed in stages, or handled by an
object-specific correlated rounding argument.

There is an even simpler obstruction to independent rounding.

### Proposition 6.2 (independent top choices have linear middle holes)

Choose one uniform cyclic order independently at every top.  For a fixed
middle owner \(X\),

\[
 \Pr(X\text{ is uncovered})=e^{-1}+o(1).
\tag{6.6}
\]

Consequently the expected number of uncovered middle owners is

\[
 (e^{-1}+o(1))W.
\tag{6.7}
\]

#### Proof

There are \(\binom mH\) tops containing \(X\).  In any one of them, the
probability that \(X\) is a cyclic \(m\)-interval is

\[
 p=\frac{m!H!}{(M-1)!}=\frac{M}{\binom Mm}.
\tag{6.8}
\]

The choices at distinct tops are independent, and

\[
 \binom mH p=\frac{MN_H}{W}=1-o(1).
\tag{6.9}
\]

Also \(p=o(1)\).  Therefore

\[
 (1-p)^{\binom mH}=e^{-1}+o(1),
\]

which proves (6.6).  Summing indicators proves (6.7).  \(\square\)

The symmetric fractional point is therefore only an intermediate step.
Independent selection, independent alteration, or a claim that fractional
feasibility itself supplies packets would leave a positive fraction of the
middle layer uncovered.

## 7. Exact implication for the constant-one construction

Assume that \(\mathcal P^{\rm aug}\) has a matching saturating every top
tag.  Forgetting the claim decorations leaves one cyclic packet per top.

1. Since \(s_m=M\), all middle intervals are matching vertices.  Hence the
   middle packets are pairwise disjoint and cover exactly
   \[
   MN_H=W-o(W)
   \]
   middle owners.

2. At rank \(k\), the matching covers exactly \(s_kN_H\) distinct claimed
   masks.  Proposition 5.2 shows that the aggregate number of uncovered
   band masks is \(o(W)\).

3. Cutting each promotion cycle once gives \(N_H\) promotion paths.  Their
   component count has the required scale because
   \[
   \frac{N_H}{W/H}=\frac{H}{\lambda_H}\le\frac HM=o(1).
   \tag{7.1}
   \]

4. Initializing each top fibre at cost at most \(2H\) gives reset toll
   \[
   2HN_H=o(W).
   \tag{7.2}
   \]

5. The ranks outside the band contain only \(o(W)\) masks in total.  Indeed,
   \[
   \frac{N_{q+1}}{N_q}=\frac{m-q}{m+q+1},
   \tag{7.3}
   \]
   so for \(q\ge H\) the tail is bounded by a geometric series:
   \[
   \sum_{q>H}N_q=O\left(\frac mH N_H\right)
   =O(W/H)=o(W).
   \tag{7.4}
   \]
   The upper tail has the same size by complementation.

Thus the literal packet paths cost

\[
 MN_H+2HN_H=W+o(W),
\]

and all band holes and outer-rank masks can be appended literally in another
\(o(W)\) entries.  This yields a direct \(W+o(W)\) OR construction.  It
does **not** assert that the literal one-entry exceptions themselves form a
\(\mathrm{CP}_A\) transversal: counted as separate path components, they
need not satisfy the stronger \(o(W/H)\) component bound.  The direct
compiler may patch the \(o(W)\) missing masks literally.  The argument uses
the actual packet flags, not an unsupported normalization of general OR
words.

## 8. The exact remaining integral lemma

The calibrated top-packet route is reduced to the following statement.

### Tag-saturating augmented packet lemma

Let \(H\) be the least integer satisfying (0.1), and form
\(\mathcal P^{\rm aug}\) using (0.6) and (5.1).  Then
\(\mathcal P^{\rm aug}\) has a matching which contains exactly one edge
above every top

\[
 U\in\binom{[2m]}{m+H}.
\tag{8.1}
\]

This is an integral assertion.  Proposition 5.1 proves its exact symmetric
fractional relaxation, including all floor capacities.  Proposition 3.1
proves the integral statement after deleting the cyclic-packet bundle
condition.  Neither result rounds the actual packet hypergraph.

A quantitatively weaker matching can also suffice, but its error must be
stated at the augmented edge scale.  If \(e\) top tags are omitted and then
filled with arbitrary packets, the worst-case aggregate claimed-mask loss is
\(O(eR_*)\).  Hence the safe near-saturation target is

\[
 e=o(W/R_*)=o(W/m^{3/2}),
\tag{8.2}
\]

not merely \(e=o(N_H)\).  Exact tag saturation avoids this extra rate issue.

The quotient in Section 3 suggests a two-stage proof attempt:

1. find one cyclic \(H\)-interval bundle at every lower tag \(R\), with the
   resulting middle complements disjoint;
2. use the remaining choice of cyclic orders and claimed starts to solve the
   rankwise capacitated transversals.

But the second step is not automatic from middle disjointness.  A lower
rank-\((m-q)\) interval is the intersection of \(q+1\) consecutive owners,
and an upper rank-\((m+q)\) interval is their union.  This is precisely the
path-hitting condition, so arbitrary middle Hall assignments do not control
the shadows.

## 9. Audit ledger

### Proved

1. \(H\sim\sqrt{m\log m}\) at the least crossing.
2. \(\lambda_H/(m+H)=1+o(1)\), with the exact overshoot bound (1.4).
3. \(MN_H=W-o(W)\) and \(HN_H=o(W)\).
4. The explicit length-\(M\) promotion cycle in every top fibre.
5. Exact exposure of every cyclic interval rank in the band.
6. The unrestricted integral top-to-middle Hall assignment.
7. All one-vertex degrees in the top-tagged packet hypergraph.
8. The exact middle pair-codegree formula (0.5).
9. The capacity-respecting claimed-slot augmentation.
10. Its exact symmetric fractional matching and exact rank deficits.
11. The aggregate floor-deficit estimate \(o(W)\).
12. The augmented edge-size asymptotic
    \((\sqrt\pi+o(1))m^{3/2}\).
13. The exact adjacent nested cross-rank codegree.
14. The \((e^{-1}+o(1))W\) independent-rounding middle-hole obstruction.
15. A tag-saturating augmented matching implies \(W+o(W)\), including the
    reset and outer-tail ledgers.

### Not proved

1. An integral middle-packet matching saturating all top tags.
2. The stronger tag-saturating augmented packet lemma.
3. Any general growing-uniformity rounding theorem applicable to this
   object.

The route is therefore neither proved nor refuted.  Its scalar capacities
and reset arithmetic are fully favorable, and the cyclic packet is exactly
legal.  The sole remaining mathematical gate is a correlated integral
near-factor which respects top tags, middle disjointness, and the claimed
interval ranks simultaneously.  The degree calculations show substantial
middle pseudorandomness; the nested-rank codegrees show why the vertical
constraints must be handled with more structure than independent rounding.

# The canonical MSW ordered portals and their exact depth-two obstruction

Date: 2026-07-25

## 0. Scope

Put

\[
n=2m+1,\qquad b=\operatorname{Cat}_m,\qquad
W=nb=\binom{2m+1}{m}.
\]

The MSW odd-graph factor consists of $b$ wreaths.  Each wreath is a cyclic
permutation of $[n]$, and its cyclic length-$m$ windows are its middle
owners.  The factor partitions all $m$-subsets.

This note concerns only the restricted singleton/FIFO interpretation in
which these cyclic words are circuits in the directed de Bruijn graph on
ordered $(m-1)$-tuples.  It makes no claim that singleton states are without
loss of generality for arbitrary OR words.

The result is deliberately local and exact:

* the all-position MSW pairs
  \[
  P1100R\longleftrightarrow P1010R
  \]
  give exactly $\operatorname{Cat}_{m-1}$ genuine ordered-state portals;
* every isolated switch at one of these portals creates, in each new seam,
  a recurrence at distance exactly $m+1$;
* for $m\ge3$, reversing or rotating the two wreaths cannot make this same
  portal depth-two safe;
* even if recurrence is ignored, this portal family alone leaves at least
  \[
  \operatorname{Cat}_m-\operatorname{Cat}_{m-1}
  =\frac{3m-3}{4m-2}\operatorname{Cat}_m
  \]
  components.

No classification of all shared ordered states of the MSW factor is claimed.
Accordingly, the last bound is an obstruction to this canonical local family,
not a global obstruction to MSW cycle splicing.

## 1. Ordered states versus unordered shadows

Let

\[
\omega=(w_0,w_1,\ldots,w_{n-1})
\]

be one wreath order.  Its directed de Bruijn edges and states are

\[
e_i=(w_i,\ldots,w_{i+m-1}),\qquad
\theta_i=(w_{i+1},\ldots,w_{i+m-1}),
\]

with cyclic indices.  The support of $e_i$ is the corresponding middle
owner.  Two circuits admit an ordinary successor switch only when they
contain the same **ordered** state $\theta$.

For an unordered set $S\in\binom{[n]}{m-1}$, suppose that $S$ occurs as a
state $\mu(S)$ times in an exact wreath factor.  At one occurrence let $a$
and $b$ be the letters immediately before and after the state.  Its two
incident middle supports are

\[
S\cup\{a\},\qquad S\cup\{b\}.
\]

Across all occurrences, these $2\mu(S)$ middle supports are distinct.
Hence all $2\mu(S)$ exterior letters are distinct and lie in the
$(m+2)$-set $[n]\setminus S$.  Therefore

\[
\boxed{\mu(S)\le \left\lfloor\frac{m+2}{2}\right\rfloor.}
\tag{1.1}
\]

For $m\ge4$ the number $(m-1)!/2$ of orders of $S$ up to reversal is at
least the right side of (1.1).  Thus even maximal unordered multiplicity
does not force equality up to reversal of two state orders.  In particular,
the unordered shadow multiplicities of the MSW factor do not by themselves
prove a successor portal.

For completeness, if $r(\theta)$ is the number of occurrences of an exact
ordered state and

\[
E_{\mathrm{ord}}=\sum_\theta (r(\theta)-1)_+,
\tag{1.2}
\]

then identifying ordered state occurrences can reduce the initial $b$
circuits by at most $E_{\mathrm{ord}}$.  Hence any unrestricted
successor-switch proof of $o(b)$ Eulerian components necessarily has

\[
E_{\mathrm{ord}}\ge b-o(b).
\tag{1.3}
\]

This is only a necessary incidence count; the collisions must also connect
almost all circuits.

## 2. The MSW tight word

For a Dyck path $x$, write its MSW flip permutation as

\[
\pi(x)=(a_0,b_0,a_1,b_1,\ldots,a_{m-1},b_{m-1})
\]

and append the distinguished coordinate $\infty$.  Reading positions with
step two in the omitted-label word gives the tight wreath order

\[
\boxed{
\omega(x)=(a_0,a_1,\ldots,a_{m-1},\infty,
                 b_0,b_1,\ldots,b_{m-1}).
}
\tag{2.1}
\]

Equivalently, up to cyclic rotation,

\[
\omega(x)=(\infty,\mathsf B(x),\mathsf A(x)).
\tag{2.2}
\]

Thus the actual MSW portal test is equality of cyclic length-$(m-1)$ words
in (2.1), not equality of their supports.

## 3. The canonical Catalan portal family

Fix

\[
0\le p\le m-2,\qquad
P\in\mathcal D_p,\qquad
R\in\mathcal D_{m-p-2},\qquad d=2p,
\]

and put

\[
X=P1100R,\qquad Y=P1010R.
\tag{3.1}
\]

The exact MSW concatenation formula, already established in
MSW_MULTIRANK_LOCAL_TRADES.md, gives cyclically rotated omitted-label
words

\[
\begin{aligned}
C&=(\delta,\beta,\gamma,\alpha,T),\\
D&=(\beta,\alpha,\delta,\gamma,T),
\end{aligned}
\tag{3.2}
\]

where

\[
\delta=d+4,\quad \beta=d+2,\quad
\gamma=d+3,\quad \alpha=d+1
\]

and

\[
T=(t_0,t_1,\ldots,t_{2m-4})
  =(d+4+\rho(R),\,n,\,\rho(P)).
\tag{3.3}
\]

Split the common tail by parity:

\[
E=(t_0,t_2,\ldots,t_{2m-4}),\qquad
O=(t_1,t_3,\ldots,t_{2m-5}).
\tag{3.4}
\]

Then $|E|=m-1$, $|O|=m-2$, and step-two reading of (3.2) gives

\[
\boxed{
\begin{aligned}
\omega_C&=(\delta,\gamma,E,\beta,\alpha,O),\\
\omega_D&=(\beta,\delta,E,\alpha,\gamma,O).
\end{aligned}}
\tag{3.5}
\]

### Theorem 3.1

The two MSW circuits indexed by $X$ and $Y$ share the exact ordered
$(m-1)$-state $E$.  Hence they admit a genuine successor switch preserving
the complete middle-owner multiset.

Across all triples $(p,P,R)$, this produces exactly

\[
\boxed{
\sum_{p=0}^{m-2}\operatorname{Cat}_p
                  \operatorname{Cat}_{m-p-2}
=\operatorname{Cat}_{m-1}}
\tag{3.6}
\]

distinct local portal occurrences.

#### Proof

The common state assertion is immediate from (3.4)--(3.5).

For fixed $p$, the word and the location of the displayed four-letter block
recover $P$ and $R$.  If two different values of $p$ gave the same unordered
pair $\{X,Y\}$, the unique four positions on which $X$ and $Y$ differ would
have two different locations, which is impossible.  The Catalan convolution
then gives (3.6).  \(\square\)

### Corollary 3.2

Suppose every switched cross pair is one of the explicitly listed pairs in
Theorem 3.1.  Then successor switching leaves at least

\[
\boxed{
\operatorname{Cat}_m-\operatorname{Cat}_{m-1}
=\frac{3m-3}{4m-2}\operatorname{Cat}_m}
\tag{3.7}
\]

Eulerian components.

#### Proof

Make an auxiliary graph on the original MSW circuits, with one edge for
each listed occurrence.  Every successor system generated using only the
listed cross-pair transpositions preserves every connected component of
this auxiliary graph, even if a transposition is reused.  A graph with
$b$ vertices and at most $\operatorname{Cat}_{m-1}$ edges has at least
$b-\operatorname{Cat}_{m-1}$ connected components, so no such successor
system can have fewer circuits.  Finally,

\[
\frac{\operatorname{Cat}_{m-1}}{\operatorname{Cat}_m}
=\frac{m+1}{4m-2}.
\]

Subtracting proves (3.7).  \(\square\)

The qualification is essential.  We have not proved that a displayed state
$E$ is absent from every third MSW circuit.  Such an additional incidence,
or any other ordered coincidence, is outside the pair family counted in
(3.6) and is not covered by (3.7).

## 4. The exact collar test for one isolated switch

Suppose two oriented wreath words have a common state

\[
\theta=(u_1,\ldots,u_{m-1})
\]

and local collars

\[
\begin{aligned}
A&=(\ldots,a_1,a_0,\theta,b_0,b_1,\ldots),\\
B&=(\ldots,c_1,c_0,\theta,d_0,d_1,\ldots).
\end{aligned}
\tag{4.1}
\]

Switching successors creates the cross seams $a_0\theta d_0$ and
$c_0\theta b_0$.

### Lemma 4.1

Let $1\le H\le m+1$, and suppose no other switch changes the displayed
radius-$(H-1)$ collars.  All words of length at most $m+H$ crossing the two
new seams have distinct letters if and only if

\[
\boxed{
a_i\ne d_j,\qquad c_i\ne b_j
\quad(i,j\ge0,\ i+j\le H-1).}
\tag{4.2}
\]

For $H=1$, these inequalities are automatic in an exact wreath factor.

#### Proof

Each original wreath is a permutation.  Since $(m-1)+H\le2m<n$, each
one-sided collar together with $\theta$ has distinct letters.  A new
repetition can therefore only compare opposite collars.  The distance from
$a_i$ to $d_j$, and from $c_i$ to $b_j$, is

\[
m+i+j.
\]

The two occurrences fit in a word of length $m+H$ precisely when
$i+j\le H-1$, proving (4.2).

For $H=1$, equality $a_0=d_0$ would repeat the middle support
$\operatorname{supp}(\theta)\cup\{a_0\}$ in two factor edges.  Exact middle
ownership forbids this, and similarly forbids $c_0=b_0$.  \(\square\)

This lemma is local.  A cluster of nearby switches must be checked using its
actual final continuations, not by applying (4.2) independently to the old
collars.

## 5. The canonical portal is orientation-completely depth-two bad

At the common state $E$ in (3.5), the collars are

\[
\begin{array}{c|cc|cc}
&a_1&a_0&b_0&b_1\\ \hline
C&\delta&\gamma&\beta&\alpha\\
D&\beta&\delta&\alpha&\gamma.
\end{array}
\tag{5.1}
\]

The two switched seams therefore contain

\[
\delta,\gamma,E,\alpha,\gamma
\tag{5.2}
\]

and

\[
\beta,\delta,E,\beta,\alpha.
\tag{5.3}
\]

### Theorem 5.1

Assume $m\ge3$.  An isolated successor switch at any canonical portal of
Theorem 3.1 has a new recurrence at distance exactly $m+1$ in each cross
seam.  It preserves distinctness of length-$(m+1)$ windows but destroys it
for a length-$(m+2)$ window.

No choice of rotations, circuit names, or orientations makes this same
portal depth-two safe.

#### Proof

In (5.2), the two copies of $\gamma$ are separated by $E$ and $\alpha$;
in (5.3), the two copies of $\beta$ are separated by $\delta$ and $E$.
Because $|E|=m-1$, both recurrence distances are $m+1$.  Lemma 4.1 with
$H=1$ excludes a shorter new recurrence.

Rotations do not change a cyclic collar.  Interchanging the two circuits
only exchanges the two seams.  Since the letters of $E$ are distinct and
$|E|=m-1\ge2$,

\[
E\ne\operatorname{rev}E.
\]

Reversing exactly one circuit therefore destroys ordered equality at this
occurrence, so it is not a switch at this portal.  Reversing both circuits
replaces $E$ by $\operatorname{rev}E$ and reverses (5.2)--(5.3); recurrence
distances are unchanged.  \(\square\)

The $m=2$ singleton-state exception is deliberately excluded from the
orientation assertion and has no asymptotic relevance.

### Corollary 5.2

In a final word with recurrence gap at least $m+2$, every used canonical
portal must be accompanied by nearby switches which alter the continuations
before the second $\gamma$ in (5.2) and before the second $\beta$ in (5.3).
Separated use of these portals is impossible.

This is a repair obligation, not a proof that a suitable clustered repair
cannot exist.

## 6. Exact residual

The canonical all-position family supplies a positive density

\[
\frac{\operatorname{Cat}_{m-1}}{\operatorname{Cat}_m}
=\frac{m+1}{4m-2}\longrightarrow\frac14
\]

of genuine ordered portals, but it neither has enough incidences for
$o(\operatorname{Cat}_m)$ components nor supplies even isolated depth-two
safe seams.

The restricted central near-Ucycle route therefore still needs one of the
following genuinely new statements:

1. an MSW-wide ordered-state incidence theorem giving
   $\operatorname{Cat}_m-o(\operatorname{Cat}_m)$ connecting portals with
   growing safe collars; or
2. a coupled local cluster theorem which repairs (5.2)--(5.3), followed by a
   proof that the repaired clusters connect all but
   $o(\operatorname{Cat}_m)$ circuits.

Unordered shadow collisions cannot replace either statement.  No global
MSW obstruction, near-Ucycle construction, shallow-shadow coverage theorem,
or coefficient-one conclusion is asserted.

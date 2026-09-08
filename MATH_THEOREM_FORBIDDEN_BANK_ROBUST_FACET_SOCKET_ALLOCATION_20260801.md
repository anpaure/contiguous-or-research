# Forbidden-bank robust facet-socket allocation

Date: 2026-08-01  
Status: unconditional set-system theorem.  It controls only distinct
rank-`r` facet owners.  It does not supply physical guard occurrences,
compatible extraction cuts, upper-deck preservation, or a chronology.

## 1. The robust allocation theorem

Let

\[
  \mathcal U\subseteq\binom{[k]}{r+1}
\]

be a family of socket targets, and let

\[
  D\subseteq\binom{[k]}r,
  \qquad |D|\le q,
\]

be an arbitrary fixed bank of protected or unavailable middle owners.  A
`D`-avoiding `b`-facet allocation assigns to each `U in mathcal U` `b`
distinct facets of `U`, uses no facet twice, and uses no member of `D`.

### Theorem 1

Assume

\[
                1\le b,\qquad b+q\le r+1,
\]

and put

\[
             s=\left\lfloor\frac{r+1}{b+q}\right\rfloor.
\]

If

\[
              |\mathcal U|\le\binom{r+s}{r+1},        \tag{1.1}
\]

then `mathcal U` has a `D`-avoiding `b`-facet allocation.

### Proof

For a nonempty subfamily `mathcal A subseteq mathcal U`, put
`a=|mathcal A|` and choose real `x>=r+1` with

\[
                       a=\binom{x}{r+1}.
\]

The Lovasz form of Kruskal--Katona gives

\[
                  |\partial\mathcal A|\ge\binom xr.
\]

Equation (1.1) implies `x<=r+s`.  Hence

\[
 \frac{|\partial\mathcal A|}{a}
 \ge \frac{\binom xr}{\binom{x}{r+1}}
 =\frac{r+1}{x-r}
 \ge\frac{r+1}{s}
 \ge b+q.                                             \tag{1.2}
\]

Deleting the protected bank loses at most `q` facets, so

\[
\begin{aligned}
 |\partial\mathcal A\setminus D|
 &\ge (b+q)a-q\\
 &=ba+q(a-1)\\
 &\ge ba.                                             \tag{1.3}
\end{aligned}
\]

Replace every `U` by `b` labelled copies and join each copy to the facets of
`U` outside `D`.  For an arbitrary collection `X` of copies, let
`mathcal A` be its underlying targets.  Then

\[
             |X|\le b|\mathcal A|
                 \le|\partial\mathcal A\setminus D|
                 =|N(X)|.
\]

Hall's theorem supplies a matching saturating all copies.  Its matched
facets are the required allocation. `square`

## 2. Protected-collar corollary

For a compact depth-`h` resident socket, take `b=h+1`.  If an independently
fixed pivot, collar, or compiler bank protects at most `q` middle owners,
then every target family satisfying

\[
 |\mathcal U|
 \le
 \binom{
   r+\left\lfloor (r+1)/(h+1+q)\right\rfloor
 }{r+1}                                               \tag{2.1}
\]

has pairwise disjoint socket facets avoiding the protected bank.

In particular, if

\[
                   h=O(\sqrt r),\qquad q=O(\sqrt r),
\]

then `s=Omega(sqrt r)`.  For sufficiently large `r`, `s>=2`.  If
`s<=r/2`, then

\[
 \binom{r+s}{r+1}
 =\binom{r+s}{s-1}
 \ge\left(\frac r{s-1}\right)^{s-1}
 =\exp(\Omega(\sqrt r\log r)).                        \tag{2.2}
\]

If `s>r/2`, monotonicity in the top parameter gives instead

\[
 \binom{r+s}{r+1}
 \ge \binom{r+\lfloor r/2\rfloor}{r+1}
 =\exp(\Omega(r)).                                    \tag{2.3}
\]

Consequently, for every fixed `C`, any family of at most `r^C` socket
targets admits disjoint facets while completely avoiding any independently
fixed `O(sqrt r)` owner bank, once `r` is sufficiently large.

More generally, the same two-case argument gives the conclusion for
polynomial target families whenever
`b+q=O(r^{1-epsilon})` for a fixed `epsilon>0`.

## 3. Interpretation and scope

The original small-family facet theorem rules out facet scarcity.  The
robust form also rules out competition with a separately fixed bounded-width
reset interface: a protected pivot/collar bank of the natural
`Theta(sqrt r)` size can be reserved first, and a polynomial socket bank can
still choose all of its middle facets afterward.

The order of quantifiers is essential.  The theorem permits an arbitrary
fixed `D`, but `D` must be known before the facet matching.  It does not
control a damage bank selected adaptively from the resulting facets.

Nor does it solve the occurrence-labelled rows that are binding in the
finite `k=17` campaign.  Even with disjoint owners, two sockets may require
incompatible component options, overlapping residence guards, destructive
extraction cuts, or child-colour providers.  Those constraints remain the
protected-host/regeneration problem.

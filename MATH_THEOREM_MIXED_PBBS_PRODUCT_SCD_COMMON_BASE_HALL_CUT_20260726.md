# Mixed PBBS/product-SCD common baseline: the exact one-seam Hall cut

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or web
input is used.

## 0. Verdict

Put

\[
 W_0=\binom{2m}{m},\qquad
 H=\lceil A\sqrt m\rceil,
 \qquad r=m-H-1,
 \tag{0.1}
\]

where \(A>0\) is fixed.  Let \(g=g(m)=o(\sqrt m)\) be the
half-width supplied by the proved sub-Gaussian PBBS word.

There is a genuine positive endpoint coupling inside every product-SCD
tail gadget.  If its two half-chain minimum ranks are \(a,b\), orient the
gadget with

\[
 p=\min(a,b),\qquad q=\max(a,b)
 \tag{0.2}
\]

on the left and right, respectively.  Then **every position of the right
chain word is already the right endpoint of a distinct middle-rank
target**.  The left chain word has

\[
 d(a,b)=m-2p
 \tag{0.3}
\]

leading singleton positions.  An ordered complementary deletion flag of
length \(d(a,b)\) absorbs all of them exactly, with no fractional choice.

The smallest local common-base relaxation, however, fails by a linear
amount.  Give a left shore access to

1. all suffix starts in the immediately preceding product gadget which
   can still have rank \(m\); and
2. one common-terminal PBBS flag of depth at most \(g\).

The number of distinct middle targets available to that shore is at most

\[
 q-p+g+1.
 \tag{0.4}
\]

Consequently its exact statewise Hall deficit is at least

\[
 \boxed{
 d(a,b)-(q-p+g+1)
 =m-a-b-g-1
 \ge H-g.}
 \tag{0.5}
\]

The equality is independent of the order in which the two half-chains
were originally named.  It is the smallest integral coupling inequality:
one prefix endpoint is one demand clone, and one admissible suffix start
can provide at most one target name because its successive unions are
nested.

There are \(\Theta_A(W_0/\sqrt m)\) Gaussian product-SCD gadgets.  After
discarding an asymptotically negligible number of non-Gaussian gadgets,
summing (0.5) gives

\[
 \boxed{\text{common-base Hall deficiency }\ge c_AW_0-o(W_0)}
 \tag{0.6}
\]

for some \(c_A>0\).  Thus the following natural mixed construction is
rigorously impossible: retain the exact product-SCD tail blocks, order
them arbitrarily, and try to absorb every left shore using only its
immediate predecessor plus one depth-\(g\) PBBS endpoint flag.

This does **not** rule out a mixed word.  It identifies its minimum
nonlocal content.  A successful word must provide

\[
 \Omega_A(W_0)
 \tag{0.7}
\]

additional ordered start states by carriers crossing at least two tail
gadgets, by genuinely interlacing PBBS positions through the tail blocks,
or by replacing the product-SCD gadgets themselves.  Merely identifying
their endpoints, even with the full proved sub-Gaussian PBBS flag, cannot
share the baseline across the Gaussian annulus.

The first, unlifted copy inside the trimmed odd lift already retains this
obstruction.  Since
\(\binom{2m+1}{m}\sim2\binom{2m}{m}\), (0.6) is also
\(\Omega_A(\binom{2m+1}{m})\) after odd normalization.  No
coefficient-one conclusion is claimed.

## 1. Product-SCD notation

Fix symmetric chain decompositions of two disjoint \(m\)-cubes.  A chain
of minimum rank \(a\) is

\[
 C_a\subset C_{a+1}\subset\cdots\subset C_{m-a}.
 \tag{1.1}
\]

For \(a>0\), write

\[
 R(C)=C_a,e_{a+1},\ldots,e_{m-a},
 \qquad
 L(C)=e_{m-a},\ldots,e_{a+1},C_a,
 \tag{1.2}
\]

where a coordinate denotes its singleton letter.  For \(a=0\), omit the
empty core and use the \(m\) singleton letters.  Every chain member is a
prefix union of \(R(C)\) and a suffix union of \(L(C)\).

For a pair \((C,D)\) with minimum ranks \(a,b\) and

\[
 a+b\le r=m-H-1,
 \tag{1.3}
\]

the standard tail gadget is \(L(C)\Vert R(D)\), in either order of the
two disjoint halves.  It covers all lower and upper tail targets whose
two half-components lie in \(C,D\).  Interchanging the two blocks does
not change this property, since set union is commutative.  We may
therefore use the favorable orientation (0.2).

The number of singleton positions before the core of \(L(C)\), when its
minimum rank is \(p>0\), is exactly

\[
 d=m-2p.
 \tag{1.4}
\]

The same formula gives \(d=m\) when \(p=0\), under the empty-core
convention.

## 2. The right shore has an exact middle baseline

### Theorem 2.1 (right-shore saturation)

Let the oriented gadget have left minimum \(p\) and right minimum \(q\),
where \(p\le q\).  For every right-chain rank represented by an actual
position,

\[
 \max(q,1)\le j\le m-q,
 \tag{2.1}
\]

the position of \(R(D)\) whose prefix union is \(D_j\) is the right
endpoint of the middle target

\[
 M_j=C_{m-j}\cup D_j.
 \tag{2.2}
\]

These targets are pairwise distinct.  Thus every right-shore position is
integrally absorbed into the middle baseline.

#### Proof

The inequalities in (2.1) and \(p\le q\) imply

\[
 p\le q\le m-j\le m-q\le m-p.
 \tag{2.3}
\]

Hence \(C_{m-j}\) exists.  Take its suffix witness in \(L(C)\), followed
by the prefix witness for \(D_j\) in \(R(D)\).  The two half-cubes are
disjoint, so the union has size

\[
 (m-j)+j=m.
\]

It ends at the displayed right position.  If \(j<j'\), then
\(D_j\ne D_{j'}\), so (2.2) gives distinct targets.  The empty-chain
endpoint convention when one minimum is zero causes no change: an empty
half-suffix is simply omitted. \(\square\)

The theorem is the positive half of the mixed construction.  No
probability, averaging, or rounding is involved.

## 3. The exact complementary-port primitive

### Lemma 3.1 (integral deletion-port completion)

Let \(z_1,\ldots,z_d\) and \(y_1,\ldots,y_d\) be pairwise distinct
coordinates, and let \(K\) be disjoint from all of them with

\[
 |K|=m-d.
 \tag{3.1}
\]

Then in the word

\[
 y_d,\ldots,y_1,K,z_1,\ldots,z_d
 \tag{3.2}
\]

every position \(z_t\) is the right endpoint of a distinct rank-\(m\)
target, namely

\[
 K\cup\{y_1,\ldots,y_{d-t}\}
   \cup\{z_1,\ldots,z_t\}.
 \tag{3.3}
\]

#### Proof

For \(t<d\), start the witnessing interval at \(y_{d-t}\); for \(t=d\),
start it at \(K\).  Its union is exactly (3.3), which has size

\[
 (m-d)+(d-t)+t=m.
\]

Successive targets exchange one \(y\)-coordinate for one
\(z\)-coordinate and are therefore distinct. \(\square\)

This is the smallest positive common-base object: the tail singleton
shore needs a complementary ordered deletion flag of the same length.
A PBBS port of depth \(g\) supplies only \(g\) deletion transitions.  The
next section proves that the missing transitions cannot be recovered from
one preceding product gadget at the Gaussian cutoff.

## 4. One-seam target capacity

We state the local model in a deliberately favorable form.  Let a
predecessor gadget have oriented minimum ranks \(p\le q\).  After its
right block, place a singleton prefix

\[
 Z_t=\{z_1,\ldots,z_t\},\qquad 1\le t\le d'.
 \tag{4.1}
\]

We allow a candidate middle witness ending at \(z_t\) to start anywhere
in the predecessor gadget.  In addition, we grant an arbitrary
common-terminal nested PBBS port with at most \(g\) further start states.
This grant ignores all physical label-compatibility restrictions and is
therefore stronger than an actual fixed PBBS port.

### Lemma 4.1 (one-seam neighbor bound)

Assume

\[
 d'<q.
 \tag{4.2}
\]

The family of distinct rank-\(m\) targets obtainable at the endpoints in
(4.1), using the allowed starts above, has cardinality at most

\[
 \boxed{q-p+g+1.}
 \tag{4.3}
\]

#### Proof

First ignore the granted PBBS port.  A witness cannot start in the new
prefix, whose union has size at most \(d'<m\).  Nor can it start in the
predecessor's right block: every suffix of that block is contained in its
maximum chain member of size \(m-q\), so after adjoining \(Z_t\) its size
is at most

\[
 m-q+t<m.
 \tag{4.4}
\]

It must therefore start in the predecessor's left block.  Such a suffix
has a chain union \(C_i\) for some \(p\le i\le m-p\).  Since the whole
right block contributes its maximum member \(D_{m-q}\), disjoint from
\(C_i\), a rank-\(m\) union is impossible when \(i>q\).  Thus only

\[
 i=p,p+1,\ldots,q
 \tag{4.5}
\]

can occur.

For a fixed start, hence fixed \(i\), the target unions obtained as
\(t\) increases are nested.  Two nested sets of the same rank are equal.
Therefore each of the \(q-p+1\) starts in (4.5) contributes at most one
distinct middle target over the whole prefix.

Exactly the same nesting argument gives at most one target name for each
additional PBBS start state.  A depth-\(g\) port has \(g+1\) states, but
its terminal state is the common state already counted in (4.5).
Consequently it contributes at most \(g\) new names.  This proves
(4.3). \(\square\)

### Corollary 4.2 (the statewise annulus deficit)

If the successor gadget has oriented minima \(p'\le q'\), its left
singleton shore has \(d'=m-2p'\) endpoint slots.  In the diagonal case
where predecessor types are merely permuted through a family of gadgets,
the total demand minus the most favorable one-seam capacity is

\[
\begin{aligned}
 \sum (m-2p)-\sum(q-p+g+1)
 &=\sum(m-p-q-g-1)\\
 &\ge (H-g)|\mathcal G|,
\end{aligned}
\tag{4.6}
\]

because every tail gadget satisfies \(p+q\le m-H-1\).

Equation (4.6) is an integral Hall inequality, not an average-load
estimate.  Each left-shore position is a demand vertex.  Its possible
rank-\(m\) target names form its neighborhood.  Distinct middle targets
need distinct right endpoints, so Hall's condition is necessary.

## 5. Gaussian-many gadgets make the cut linear

We now remove the technical hypothesis (4.2) from all but a negligible
number of gadgets.

Put

\[
 \ell=\lfloor m/2\rfloor,
 \qquad \epsilon=m-2\ell,
 \qquad T=\left\lceil\sqrt{3m\log m}\right\rceil.
 \tag{5.1}
\]

Call a chain Gaussian-bulk if its minimum rank is at least \(\ell-T\),
and call a tail gadget bulk if both of its chains are bulk.  For a bulk
gadget,

\[
 q\ge\ell-T>m/3,
 \qquad
 d=m-2p\le\epsilon+2T<m/3
 \tag{5.2}
\]

for all sufficiently large \(m\).  Hence (4.2) holds whenever a bulk
gadget follows another bulk gadget.

Let

\[
 A_m(a)=\binom ma-\binom m{a-1}
 \tag{5.3}
\]

be the number of half-cube chains of minimum rank \(a\).  Telescoping
gives

\[
 \sum_{a=0}^{\ell-T-1}A_m(a)=\binom m{\ell-T-1}.
 \tag{5.4}
\]

The central-binomial ratio bound yields

\[
 \frac{\binom m{\ell-T-1}}{\binom m\ell}
 \le \exp\!\left(-\frac{(T+1)^2}{m}\right)
 =O(m^{-3}).
 \tag{5.5}
\]

Thus the number \(E_m\) of nonbulk ordered chain pairs is at most

\[
 E_m
 \le 2\binom m{\ell-T-1}\binom m\ell
 =O\!\left(m^{-3}\binom m\ell^2\right)
 =o(W_0/m).
 \tag{5.6}
\]

The last equality follows from Wallis/Stirling,

\[
 \binom m\ell^2=\Theta(W_0/\sqrt m).
 \tag{5.7}
\]

The restriction \(a+b\le r\) can only decrease \(E_m\).

In the other direction, there are Gaussian-many bulk tail gadgets.  Fix

\[
 U=A+2
 \tag{5.8}
\]

and take integers

\[
 U\sqrt m\le x,y\le(U+1)\sqrt m,
 \qquad a=\ell-x,\quad b=\ell-y.
 \tag{5.9}
\]

For large \(m\), these ranks are positive and bulk, and

\[
 a+b=m-\epsilon-x-y\le m-H-1.
 \tag{5.10}
\]

Uniformly on the fixed interval in (5.9),

\[
\begin{aligned}
 A_m(\ell-x)
 &=\binom m{\ell-x}
   \frac{2x+\epsilon+1}{\ell+x+\epsilon+1}\\
 &=\Theta_A(2^m/m).
\end{aligned}
\tag{5.11}

There are \(\Theta(m)\) pairs \((x,y)\) in (5.9).  Hence the number
\(G_m\) of bulk tail gadgets satisfies

\[
 G_m\ge c_A\frac{4^m}{m}
      \ge c_A'\frac{W_0}{\sqrt m}
 \tag{5.12}
\]

for constants \(c_A,c_A'>0\).

Order all tail gadgets arbitrarily.  A bulk successor with a bulk
predecessor obeys Lemma 4.1.  There are at most \(E_m\) bulk successors
with a nonbulk predecessor, and at most one initial bulk gadget with no
predecessor; grant every one of their at most \(m\) demands for free.  If
\(\mathcal P\) is the set of all leading singleton
positions of bulk left shores and \(\mathcal N(\mathcal P)\) is their
rank-\(m\) target neighborhood in the one-seam-plus-one-PBBS-port model,
then

\[
\begin{aligned}
 |\mathcal P|-|\mathcal N(\mathcal P)|
 &\ge
 \sum_{e\ {\rm bulk}}(m-p_e-q_e-g-1)-m(E_m+1)\\
 &\ge (H-g)G_m-o(W_0)\\
 &\ge c_A''W_0-o(W_0).
\end{aligned}
\tag{5.13}
\]

Here \(H-g=(A+o(1))\sqrt m\), and (5.6), (5.12) give the last two
lines.  This proves (0.6).

## 6. Why Hall deficiency is literal word excess

In any literal word, two distinct targets of one antichain cannot have
the same right endpoint: intervals with a common right endpoint have
nested unions.  Therefore covering all \(W_0\) middle sets requires
\(W_0\) distinct endpoint positions.

Suppose a mixed word retains the product-SCD tail positions and restricts
the witnesses ending at \(\mathcal P\) to the local model above.  By
(5.13), at least \(c_A''W_0-o(W_0)\) of those positions cannot be assigned
distinct middle targets.  All remaining word positions can contribute at
most one new middle endpoint each.  Hence the total word length is at
least

\[
 W_0+c_A''W_0-o(W_0).
 \tag{6.1}
\]

The proved PBBS sub-Gaussian theorem certifies targets only through depth
\(g=o(\sqrt m)\); by itself it certifies no longer ordered deletion
port.  Lemma 4.1 grants the full depth-\(g\) port in the most favorable
form.  Therefore that theorem does not overlap the exact product-SCD tail
merely by matching one certified endpoint flag or one baseline state per
gadget.  A particular PBBS word may have additional starts whose
witnesses travel far outside this local flag.  Those are nonlocal
carriers and lie deliberately outside the no-go.

For the standard trimmed odd lift, its first copy is the original even
tail word.  Apply (5.13) to that copy alone; later bridge and translated
positions cannot create new right-endpoint witnesses at earlier
positions.  Since

\[
 \binom{2m+1}{m}\sim2W_0,
\]

the normalized obstruction remains a positive \(A\)-dependent constant.

## 7. Exact boundary

The following statements are proved.

* Every right shore of the exact product-SCD tail has a complete integral
  middle-endpoint assignment.
* A complementary deletion flag of the same length gives an exact
  positive completion of a left singleton shore.
* Immediate-predecessor starts and one common depth-\(g\) PBBS flag obey
  the exact Hall capacity (4.3).
* At the Gaussian cutoff, the resulting deficit is at least \(H-g\) per
  gadget and \(\Omega_A(W_0)\) in total.

Accordingly the smallest surviving positive statement is now precise:
construct a nonlocal ordered-deletion flow which supplies the missing
\(\Omega_A(W_0)\) start states while using only \(o(W_0)\) additional
positions.  Such a flow must let one carrier pass through several
product-SCD gadgets or must interlace the PBBS word inside their singleton
shores.  A one-gadget endpoint matching, even with arbitrary target
relabeling and the entire sub-Gaussian PBBS port, is ruled out.

This report does not rule out that nonlocal flow and does not prove the
constant-one theorem.

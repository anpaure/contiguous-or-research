# The ladder-aware TRP nibble at \(\ell=\lfloor m^{3/5}\rfloor\)

Date: 2026-07-25

Pure mathematics only.  No computation, solver, web input, or
fixed-uniformity matching theorem is used.

## 0. Verdict

Put

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q},\qquad
 \ell=\lfloor m^{3/5}\rfloor,
\]

and retain the calibrated parameters \(H,M=m+H,Q\).  Let

\[
 J=\left\lfloor {M\over\ell}\right\rfloor,
 \qquad T=JN_H,
 \qquad S=\ell T.
\tag{0.1}
\]

Thus \(T=(1+o(1))W/\ell\) is the number of labelled carrier copies and
\(S=W-O(W\ell/m)\) is the number of flag occurrences in every tagged
row.

Call a tagged row **hard** when its physical target count is at least
\(S\).  If \(b\) is the number of hard rows, then

\[
 b=2q_*+1=O(\sqrt\ell),
 \qquad
 R:=b\ell=O(\ell^{3/2})=O(m^{9/10}).
\tag{0.2}
\]

The exact nested-pair formula does permit a rigorous first nibble bite.
After a nonempty invariant support restriction, every candidate chunk
has \(R\) hard flag resources and one left carrier-copy resource, and its
conflict neighbourhood has size

\[
 \boxed{|\Gamma(e)|=(1+o(1))R\mathcal D,}
\tag{0.3}
\]

where \(\mathcal D\) is the common catalogue size above one carrier copy.
Consequently, independently marking candidates with probability

\[
 p={\theta\over R\mathcal D}
\]

and retaining the isolated marks gives

\[
 \boxed{
 \mathbb E|\mathcal M_1|
   =(\theta e^{-\theta}+o(1)){T\over R}.}
\tag{0.4}
\]

There is also a one-bite conditional degree-variance bound with error

\[
 \sigma_\ell
 =O\!\left({\ell\over m}+{R\ell\over m^2}\right)
 =O(m^{-2/5})=o(1).
\tag{0.5}
\]

However, the same calculation **refutes literal vertical contraction**.
Among candidates which conflict with a fixed chunk on a hard target, all
but an \(o(1)\) fraction share exactly one hard target with it.  The
triangular deletion/addition ladder therefore does not behave like
\(\ell\) indivisible column claims.  It behaves, at the first-bite scale,
like \(R=b\ell\) separate exclusion resources.  In particular, marking at
the proposed contracted scale \(1/(\ell\mathcal D)\) gives isolation
probability

\[
 \exp(-(1+o(1))\theta b),
\tag{0.6}
\]

not \(e^{-\theta+o(1)}\).

This note proves a clean iterative residual theorem: if the successive
residual catalogues satisfy an explicit ladder-residual closure condition
for \(O(R\log Q)\) bites, then the number \(u\) of unmatched carrier copies
satisfies

\[
 \boxed{u=o\!\left({W\over Q\ell}\right),}
\tag{0.7}
\]

and the aggregate hard-band flag leave is \(o(W)\).  The initial TRP
catalogue satisfies the first-bite hypotheses, but the residual closure is
not proved by the pair formula.  Shifted chunks have common hard-flag cores
of size \(R-b\), so propagation requires a weighted higher-link estimate.
For a quasirandom product residual, the catalogue is in fact exhausted
before (0.7) whenever \(b\ge4\).

Thus the exact remaining discrepancy is now narrow:

> construct an owner-dependent, vertically aligned sequence of residual
> catalogues satisfying the closure condition in Theorem 7.1, or prove a
> weighted common-core hierarchy which supplies it.

The formula \(c_h(\ell)/(\ell\binom sr)\) proves the first bite and locates
this discrepancy.  It does not by itself contract the ladder or justify
the iteration.

## 1. Hard and monitored rows

For a tagged row \(\alpha\), write

\[
 n_\alpha=\binom{2m}{r_\alpha},
 \qquad
 \mu_\alpha={S\over n_\alpha}.
\tag{1.1}
\]

The hard rows are

\[
 \mathcal A_{\rm h}=\{\alpha:\mu_\alpha\le1\}.
\tag{1.2}
\]

They form the symmetric interval of ranks
\(m-q_*,\ldots,m+q_*\).  Since

\[
 {S\over W}=1-O\!\left({H+\ell\over m}\right)
             =1-O(\ell/m)
\tag{1.3}
\]

and

\[
 \log{W\over N_q}\ge {q^2\over m+q},
\tag{1.4}
\]

the inequality \(N_q\ge S\) implies \(q=O(\sqrt\ell)\).  This proves
(0.2).  Moreover, uniformly on hard rows,

\[
 1-O(\ell/m)\le\mu_\alpha\le1.
\tag{1.5}
\]

Rows outside \(\mathcal A_{\rm h}\) are called **monitored**.  They have
\(\mu_\alpha\ge1\).  Hard targets are exclusion resources: no two selected
chunks may use the same one.  Monitored targets need only be hit at least
once; repeated hits there are harmless.

This hard/monitored split is essential.  Making every one of the
\((2Q+1)\ell\) flag slots an exclusion resource reproduces the obstruction
in Section 13 of `TRP_OWNER_PATH_CODEGREE_AUDIT_20260725.md`.  Treating all
outer targets as unmonitored, on the other hand, leaves their coverage
unproved.

## 2. The clean structured catalogue

For each labelled carrier copy \(\xi=(U,j)\), begin with the stationary
length-\(\ell\) rotor chunks in \(U\).  Make the following invariant
restrictions.  The restriction is used for exact support counting; no
claim is made that it retains a \(1-o(1)\) fraction after every high row is
made simple.

1. In every tagged row, a chunk uses each physical target at most once.
2. Between two hard rows, a containment between two targets of the chunk
   is allowed only at one of the path-forced offsets.

Call the resulting chunks **clean**, and let \(\mathscr P_\xi\) be their
catalogue.  Coordinate permutations preserve cleanliness.  Every carrier
is isomorphic to every other carrier, so

\[
 |\mathscr P_\xi|=\mathcal D
\tag{2.1}
\]

is independent of \(\xi\).

The catalogue is nonempty.  Indeed, take a cyclic order on \(U\) and an
\(\ell\)-state segment of its sliding-window packet.  Since
\(\ell<M\), every proper cyclic interval in a fixed rank is different.
For cyclic intervals of lengths \(r<s\), containment occurs at precisely
the \(s-r+1\) relative starts prescribed by the path offsets.  Thus this
segment satisfies both restrictions.

The second restriction is also negligible if imposed before the
all-row-simple restriction.  For hard depths \(q\le q_*=o(Q)\), the exact
deletion/addition sequences rule out an unforced containment at time
separation at most \(Q\).  At a larger separation, containment places the
two middle owners at Johnson distance \(O(q_*)\); the coupon-return bound
from Lemma 5.1 of `TRP_OWNER_PATH_CODEGREE_AUDIT_20260725.md` gives
probability \(e^{-\Omega(Q)}\).  A union bound over
\(O(b^2\ell^2)\) row/time pairs preserves \(e^{-\Omega(Q)}\).

More explicitly, write a geodesic owner segment as

\[
 X_{t+i}=X_t-\{a_{t+1},\ldots,a_{t+i}\}
              +\{c_{t+1},\ldots,c_{t+i}\}.
\tag{2.1a}
\]

Then the lower flag is

\[
 L_q(t)=X_t-\{a_{t+1},\ldots,a_{t+q}\},
\tag{2.1b}
\]

while the upper flag is obtained by adjoining the corresponding ordered
past-departure sequence to \(X_t\).  Comparing these ordered deletion and
addition lists gives exactly the offsets \(0,1,\ldots,h\) for ranks
separated by \(h\).  If a purported containment at lag at most \(Q\) is
not one of these, containment first forces the two owners to be at
distance \(O(q_*)\); geodesicity then forces the lag to be \(O(q_*)\), so
all lists involved lie inside one \(Q\)-step geodesic segment and the
direct comparison is valid.

Every clean chunk contains exactly \(\ell\) distinct targets in every
tagged row.  Double counting and coordinate transitivity therefore give
the exact degree identities

\[
 d(\xi)=\mathcal D,
 \qquad
 d(\alpha,A)=\mu_\alpha\mathcal D.
\tag{2.2}
\]

For a candidate chunk \(e\), let \(C(e)\) be its hard-target set.  Then

\[
 |C(e)|=R=b\ell.
\tag{2.3}
\]

## 3. The exact ladder pair count

Take two hard rows of ranks \(r<s\), and put \(h=s-r\).  A resident chunk
has exactly

\[
 c_h(\ell)
 =\sum_{d=0}^h(\ell-d)
 =(h+1)\ell-\binom{h+1}{2}
\tag{3.1}
\]

path-forced nested slot pairs.  Cleanliness says that these are all its
nested pairs between the two rows.

### Lemma 3.1 (exact clean-catalogue codegree)

For fixed nested targets \(A\subset B\), \(|A|=r\), \(|B|=s\),

\[
 \boxed{
 {d((r,A),(s,B))\over d(s,B)}
 ={c_h(\ell)\over\ell\binom sr}.}
\tag{3.2}
\]

#### Proof

There are \(T\mathcal D\) clean candidate chunks.  Each contributes exactly
\(c_h(\ell)\) nested pairs in the two rows.  The coordinate group is
transitive on the

\[
 \binom{2m}{s}\binom sr
\]

nested physical pairs.  Hence the numerator in (3.2) is

\[
 {T\mathcal D c_h(\ell)
  \over \binom{2m}{s}\binom sr}.
\]

By (2.2), the denominator is

\[
 {T\mathcal D\ell\over\binom{2m}{s}}.
\]

Division proves (3.2). \(\square\)

For adjacent rows this is

\[
 {2\ell-1\over\ell(s)}={2+o(1)\over m}.
\tag{3.3}
\]

For \(h\ge2\), it is at most

\[
 O\!\left({(h+1)h!\over m^h}\right).
\tag{3.4}
\]

For a nonnested pair in two near-middle rows, or for two distinct targets
in one row, the relevant coordinate orbit has size \(\Omega(m^2)\).
The time-pair orbit argument therefore gives

\[
 {d(u,v)\over\mathcal D}=O(\ell/m^2).
\tag{3.5}
\]

Equation (3.2), rather than the generic \(O(\ell/m)\) orbit bound, is the
gain supplied by the ladder.

## 4. Pair energy of one structured claim

Let \(e\) be a clean candidate.  Sum the codegrees of the hard resources
which occur in \(e\).  Structural nested pairs contribute, by
(3.1)--(3.4),

\[
 \begin{aligned}
 {1\over\mathcal D}
 \sum_{\substack{\{u,v\}\subset C(e)\\u\subset v
                   \text{ structurally}}}d(u,v)
 &\le
 C\sum_{h=1}^{b-1}(b-h)
 {c_h(\ell)^2\over\ell\binom{m-O(q_*)}{h}}\\
 &=O(R/m).
 \end{aligned}
\tag{4.1}
\]

The term \(h=1\) dominates.  There are at most \(R^2/2\) remaining hard
pairs in \(e\), so (3.5) gives

\[
 {1\over\mathcal D}
 \sum_{\substack{\{u,v\}\subset C(e)\\
                   \text{not structurally nested}}}d(u,v)
 =O(R^2\ell/m^2).
\tag{4.2}
\]

Since \(R=O(\ell^{3/2})\),

\[
 {1\over R\mathcal D}
 \sum_{\{u,v\}\subset C(e)}d(u,v)
 =O\!\left({1\over m}+{R\ell\over m^2}\right)
 =O(m^{-1/2})=o(1).
\tag{4.3}
\]

Pairs involving the left vertex \(\xi(e)\) are smaller.  Proposition
11.2 of `TRP_OWNER_PATH_CODEGREE_AUDIT_20260725.md` gives

\[
 {d(\xi,(\alpha,A))\over\mathcal D}
 ={\ell\over\binom M{r_\alpha}}
\tag{4.4}
\]

when \(A\subset U\), and zero otherwise.  Uniformly for controlled ranks,
the sum of (4.4) over the polynomially many resources of \(e\) is \(o(1)\).

Combining (4.3)--(4.4), the same estimate holds after the left resource is
adjoined:

\[
 \boxed{
 {1\over R\mathcal D}
 \sum_{\{u,v\}\subset \{\xi(e)\}\cup C(e)}d(u,v)
 =O\!\left({1\over m}+{R\ell\over m^2}\right)=o(1).}
\tag{4.5}

## 5. No literal column contraction

Let \(\Gamma(e)\) be the candidate chunks which either have the same left
carrier-copy vertex as \(e\), or share at least one hard target with
\(e\).  By (1.5) and (2.2),

\[
 \sum_{v\in\{\xi(e)\}\cup C(e)}d(v)
 =(1+o(1))R\mathcal D.
\tag{5.1}
\]

The union bound gives the same expression as an upper bound for
\(|\Gamma(e)|\).  Bonferroni, (4.4), and (4.5) give it as a lower bound.
Thus

\[
 \boxed{|\Gamma(e)|=(1+o(1))R\mathcal D.}
\tag{5.2}
\]

There is a sharper interpretation.  Let \(B_2(e)\) be the candidates
sharing at least two hard targets with \(e\).  Then

\[
 |B_2(e)|
 \le\sum_{\{u,v\}\subset C(e)}d(u,v)
 =o(R\mathcal D).
\tag{5.3}
\]

On the other hand, the hard-target part of \(\Gamma(e)\) has size
\((1+o(1))R\mathcal D\).  Therefore

\[
 \boxed{
 { |B_2(e)|\over
   |\{f:C(e)\cap C(f)\ne\varnothing\}|}=o(1).}
\tag{5.4}
\]

So, conditional on a hard conflict with \(e\), a candidate \(f\) shares
exactly one hard target with probability \(1-o(1)\).

This is the exact counterterm to vertical contraction.  The deletion and
addition flags do form one connected triangular ladder:

\[
 L_q(t)\subset L_{q-1}(t),\quad
 L_q(t)\subset L_{q-1}(t+1),
\tag{5.5}
\]

with the analogous two-parent relations on the upper side.  Contracting
all these forced relations literally contracts the whole chunk ladder.
But (5.4) shows that external conflicts do not arrive as whole-ladder, or
even two-rung, conflicts.  Almost every external conflict hits one tagged
resource only.

In particular, if candidates are marked with probability
\(p=\theta/(\ell\mathcal D)\), then (5.2) gives

\[
 \Pr(e\text{ is isolated}\mid e\text{ marked})
 =\exp(-(1+o(1))\theta R/\ell)
 =\exp(-(1+o(1))\theta b).
\tag{5.6}
\]

Thus a column-contracted isolated-edge nibble already has the wrong scale
in its first bite.

## 6. The rigorous one-bite theorem

Fix \(0<\theta\le1\), independently mark every clean candidate with

\[
 p={\theta\over R\mathcal D},
\tag{6.1}
\]

and retain a marked candidate exactly when no other marked candidate lies
in its conflict neighbourhood.  The retained candidates form a matching
on the left vertices and all hard targets.

### Theorem 6.1 (ladder-aware first bite)

The expected number of retained chunks is

\[
 \boxed{
 \mathbb E|\mathcal M_1|
 =(\theta e^{-\theta}+o(1)){T\over R}.}
\tag{6.2}
\]

#### Proof

There are \(T\mathcal D\) candidates.  For a fixed \(e\),

\[
 \Pr(e\text{ retained})
 =p(1-p)^{|\Gamma(e)|-1}.
\]

By (5.2),

\[
 p|\Gamma(e)|=\theta+o(1),
 \qquad
 p^2|\Gamma(e)|=o(1).
\]

Hence the last probability is
\((\theta e^{-\theta}+o(1))/(R\mathcal D)\), uniformly in \(e\).
Summing over the candidates proves (6.2). \(\square\)

There is also a useful monitored-target statement.  Suppose a physical
target \(z\) in a monitored row has clean-catalogue support degree

\[
 d(z)=\nu_z\mathcal D,
 \qquad 1\le\nu_z\le\mu_{\max},
 \qquad \mu_{\max}=o(R).
\tag{6.3}
\]

The all-row-simple symmetric catalogue has \(\nu_z=\mu_\alpha\), and here

\[
 \mu_{\max}\le\mu_Q
 \le (1+o(1))\lambda_Q
 =\log m\,e^{\gamma+o(1)}=m^{o(1)}=o(R).
\tag{6.4}
\]

Let \(Y_z\) count retained chunks containing \(z\), where equality at
\(z\) itself is not declared a conflict.  The proof above gives

\[
 \mathbb EY_z
 =(\theta e^{-\theta}+o(1)){\nu_z\over R}.
\tag{6.5}
\]

Also

\[
 \mathbb E\binom{Y_z}{2}
 \le p^2d(z)^2/2=O(\nu_z^2/R^2).
\tag{6.6}
\]

Bonferroni and \(\nu_z=o(R)\) imply

\[
 \boxed{
 \Pr(z\text{ is hit in the bite})
 \ge(\theta e^{-\theta}+o(1)){\nu_z\over R}.}
\tag{6.7}
\]

### Proposition 6.2 (one-bite hard-degree stability)

Delete every left or hard resource lying in any marked candidate, whether
or not the candidate is retained.  Fix such a vertex \(v\), condition on
\(v\) not being deleted, and let \(Z_v\) be its degree in the untouched
catalogue.  Then

\[
 \mathbb E Z_v=(1+o(1))d(v)e^{-\theta}
\tag{6.8}
\]

and

\[
 \boxed{
 {\operatorname {Var}Z_v\over\mathcal D^2}
 =O\!\left({1\over\mathcal D}+\sigma_\ell+{\ell\over m}\right),
 \quad
 \sigma_\ell=O\!\left({\ell\over m}+{R\ell\over m^2}\right)=o(1).}
\tag{6.9}
\]

#### Proof

For a candidate \(g\) avoiding \(v\), put

\[
 A_g(v)=\#\{e:e\ni v,\ C(e)\cap C(g)\ne\varnothing\}.
\]

The union bound gives

\[
 A_g(v)\le\sum_{u\in C(g)}d(u,v).
\tag{6.10}
\]

If \(v\) and \(u\) are in adjacent rows and nested, (3.2) contributes
\(O(1/m)\) after normalization by \(\mathcal D\); there are at most
\(\ell\) choices for \(u\) in that row of \(g\).  Larger structural
separations sum to less.  Every nonstructural pair contributes
\(O(\ell/m^2)\) by (3.5), and \(g\) has \(R\) hard resources.  Hence

\[
 \max_g A_g(v)\le\sigma_\ell\mathcal D.
\tag{6.11}
\]

Moreover,

\[
 \sum_g A_g(v)\le R\mathcal D\,d(v)=O(R\mathcal D^2).
\tag{6.12}
\]

Write \(Z_v=\sum_{e\ni v}I_e\), where \(I_e\) is the event that no marked
candidate outside the star of \(v\) conflicts with \(e\).  Equation (5.2)
gives (6.8).  For two candidates \(e,f\ni v\), independence of marks gives

\[
 0\le\operatorname {Cov}(I_e,I_f)
 \le Cp\,|\Gamma(e)\cap\Gamma(f)\setminus E(v)|.
\]

Summing first over the conflicting candidate \(g\) gives

\[
 \sum_{e,f\ni v}|\Gamma(e)\cap\Gamma(f)\setminus E(v)|
 =\sum_g A_g(v)^2
 \le\sigma_\ell\mathcal D\sum_gA_g(v).
\]

Use (6.1) and (6.12).  The off-diagonal covariance is
\(O(\sigma_\ell\mathcal D^2)\), while the diagonal variance is
\(O(\mathcal D)\).  The term \(O(\ell/m)\) records the initial hard-row
degree imbalance (1.5).  This proves (6.9). \(\square\)

Proposition 6.2 proves genuine one-step stability.  It does not propagate
the high links needed to apply itself for \(R\log Q\) rounds.

## 7. An iterative residual theorem

We now state the exact closure property needed for iteration.  It is
deliberately a property of residual catalogues, not a disguised assertion
that pair codegrees automatically propagate.

### Definition 7.1 (ladder-residual closure, LRC)

A residual instance consists of active left vertices, unused hard targets,
uncovered monitored targets, and the clean candidates avoiding the used
hard targets.  It has \(\operatorname {LRC}(R,\mathcal D_t,\varepsilon_t)\)
when:

1. every active left vertex has degree
   \((1\pm\varepsilon_t)\mathcal D_t\);
2. every admissible candidate \(e\) has hard-conflict neighbourhood
   \[
    |\Gamma_t(e)|=(1\pm\varepsilon_t)R\mathcal D_t;
   \]
3. every uncovered monitored target \(z\) has support degree between
   \((1-\varepsilon_t)\mathcal D_t\) and
   \(\mu_{\max}\mathcal D_t\), where \(\mu_{\max}=o(R)\);
4. \(R\mathcal D_t\to\infty\), and
   \(\sup_t\varepsilon_t=o(1)\).

### Theorem 7.1 (iterated residual bite)

Assume that every residual produced by the isolated-edge bite satisfies
LRC for

\[
 s=\left\lceil {8e^\theta\over\theta}R\log Q\right\rceil
\tag{7.1}
\]

successive rounds.  Then there is a sequence of bites after which

\[
 u=o(T/Q)=o\!\left({W\over Q\ell}\right)
\tag{7.2}
\]

left vertices remain unmatched and the number of uncovered monitored
targets is \(o(W)\).

#### Proof

At round \(t\), mark every admissible candidate with probability

\[
 p_t={\theta\over R\mathcal D_t}
\]

and retain isolated marks.  Put \(a=\theta e^{-\theta}\).  LRC and the
calculation in Theorem 6.1 show that, conditional on the history, every
active left vertex is matched in that round with probability at least

\[
 {a\over2R}
\tag{7.3}
\]

for all sufficiently large \(m\).

For an uncovered monitored target, repeat (6.5)--(6.7).  Its lower support
degree is \((1-o(1))\mathcal D_t\), and its upper support degree is
\(o(R)\mathcal D_t\).  Therefore it too is hit with conditional
probability at least \(a/(2R)\).

After \(s\) rounds, a fixed left vertex or monitored target survives with
probability at most

\[
 \left(1-{a\over2R}\right)^s
 \le e^{-as/(2R)}
 \le Q^{-4}.
\tag{7.4}
\]

There are \(T\) left vertices.  There are at most \((2Q+1)W\) monitored
targets.  Hence

\[
 \mathbb Eu\le TQ^{-4},
 \qquad
 \mathbb E h_{\rm mon}\le(2Q+1)WQ^{-4}.
\tag{7.5}
\]

Apply the probabilistic method to the nonnegative normalized sum

\[
 {u\over T/Q}+{h_{\rm mon}\over W}.
\]

Its expectation is \(O(Q^{-3})\), so some outcome makes both terms
\(o(1)\).  This proves (7.2) and the monitored-target conclusion.
\(\square\)

## 8. Why the left bound is exactly the needed bound

Suppose Theorem 7.1 applies.  In a hard row \(\alpha\), the selected
matching uses distinct targets, so before the unmatched carrier copies are
filled the number of holes is

\[
 n_\alpha-\ell(T-u)
 =(n_\alpha-S)+\ell u.
\tag{8.1}
\]

Since \(n_\alpha\le W\),

\[
 \sum_{\alpha\in\mathcal A_{\rm h}}(n_\alpha-S)
 \le b(W-S)
 =O\!\left({W\ell^{3/2}\over m}\right)
 =O(Wm^{-1/10})=o(W).
\tag{8.2}
\]

The unmatched contribution over all controlled rows is at most

\[
 (2Q+1)\ell u.
\tag{8.3}
\]

Therefore

\[
 u=o\!\left({W\over Q\ell}\right)
\]

is precisely sufficient to make (8.3) \(o(W)\).  It is stronger by the
factor \(Q\) than the owner-only requirement \(u=o(W/\ell)\).

The reset toll is

\[
 O(QT)=O(QW/\ell)=o(W),
\tag{8.4}
\]

and the carrier remainders cost \(O(W\ell/m)=o(W)\).  Thus LRC plus
Theorem 7.1 would give the coefficient-one ledger.

## 9. Why LRC is not proved by the first-bite calculation

There are two independent obstructions.

### 9.1 Long common ladder cores

Take a cyclic-packet rotor walk

\[
 \omega_0,\omega_1,\ldots,\omega_\ell.
\]

All relevant row targets in this \((\ell+1)\)-state segment are distinct.
Its two shifted \(\ell\)-state chunks use the same flags at states
\(\omega_1,\ldots,\omega_{\ell-1}\).  On the hard rows their common core
has size exactly

\[
 b(\ell-1)=R-b.
\tag{9.1}
\]

Assign the two chunks to distinct labelled copies of the same carrier.
They are legitimate distinct candidates.  Thus no deterministic
\(O(1)\) intersection bound exists.

For two candidates \(e,f\) with a common core of size \(k\), Bonferroni
and (4.5) give

\[
 |\Gamma(e)\cap\Gamma(f)|\ge(1-o(1))k\mathcal D.
\]

The exact second moment of a residual pair link consequently contains the
factor

\[
 (1-p_t)^{-|\Gamma_t(e)\cap\Gamma_t(f)|}
 \ge \exp\!\left(\Omega\!\left({k\over R}\right)\right).
\tag{9.2}
\]

At \(k=R-b\), this is bounded away from one in every bite.  Its frequency
may be tiny, but (3.2) controls only two prescribed target vertices and
does not calculate that frequency.  A full iteration must therefore bound
the weighted overlap enumerator

\[
 \Psi_j(e)
 ={1\over\mathcal D}
   \sum_{\substack{f:\xi(f)\ne\xi(e)}}
   \binom{|C(e)\cap C(f)|}{j},
\tag{9.3}
\]

uniformly through residuals, with weights increasing exponentially in
\(j/R\).  This is the ladder version of the missing higher-link hierarchy
in `MATH_ATTACK_TRP_SHORT_CHUNK_NIBBLE_AUDIT_20260725.md`.

### 9.2 Product-residual degree exhaustion

The full stationary catalogue satisfies

\[
 \mathcal D\le P_\ell
 ={M!\over(m-Q)!(H-Q)!}
   \bigl((m-Q)(H-Q)\bigr)^{\ell-1}.
\tag{9.4}
\]

Because \(H=m^{1/2+o(1)}\), \(Q=o(\ell)\), and
\(\ell=m^{3/5+o(1)}\),

\[
 \log P_\ell=(3/2+o(1))\ell\log m.
\tag{9.5}
\]

If unused hard targets form a quasirandom product residual of density
\(z\), a candidate survives with probability \(z^R\).  Reaching the
left-unmatched fraction \(z=1/Q\) would leave expected degree at most

\[
 P_\ell Q^{-R}.
\tag{9.6}
\]

Since \(\log Q=(1/2+o(1))\log m\),

\[
 \log(P_\ell Q^{-R})
 \le
 \left({3\over2}-{b\over2}+o(1)\right)\ell\log m.
\tag{9.7}
\]

Thus for \(b\ge4\), and in particular whenever \(b\to\infty\), the
product residual has asymptotically no candidate per left vertex long
before the required leave is reached.  This does not rule out a specially
aligned integral residual.  It proves that LRC cannot be obtained by an
ordinary quasirandom thinning argument.

## 10. Exact remaining gate

The coefficient-one route at \(\ell=m^{3/5}\) is therefore reduced to the
following non-generic statement.

> **Aligned ladder-residual gate.**  Choose the bites, or choose an
> equivalent global integral family of chunks, so that the unused hard
> target sets remain vertically aligned and the residual catalogues satisfy
> LRC for \(O(R\log Q)\) rounds, while every uncovered monitored target
> retains support degree at least the current left degree.

The initial exact nested formula proves:

1. adjacent ladder codegree \((2+o(1))/m\);
2. the aggregate pair-energy estimate (4.5);
3. the true conflict scale \(R\mathcal D\);
4. the first-bite theorem (6.2);
5. one-bite hard-degree stability (6.9).

It also proves, through (5.4), that simply declaring a vertical column to
be one claim is not a valid contraction.  The unproved object is an
**aligned residual**, not another scalar pair-codegree estimate.  Its
integral discrepancy is measured exactly by failure of one of the four
LRC clauses, equivalently by an uncontrolled weighted common-core sum
(9.3) or by loss of monitored-target support.

This is the sharp coefficient-one audit at the requested chunk length.

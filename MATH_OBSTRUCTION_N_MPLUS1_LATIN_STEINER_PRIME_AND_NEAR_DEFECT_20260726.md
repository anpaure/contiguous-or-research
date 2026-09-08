# The \((m+1)\)-colour local-pair engine: prime admissibility, automatic resolution, and the quantitative residue floor

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Result

Use the notation and local pair maps of
MATH_THEOREM_N_MPLUS1_EDGE_COLOR_PAIR_LATIN_ENGINE_20260726.md.
Thus

\[
 {\cal L}=\binom{[2m]}{m-1},\qquad
 {\cal M}=\binom{[2m]}m,\qquad
 {\cal U}=\binom{[2m]}{m+1},
\]

\[
 n=m+1,\qquad N=|{\cal L}|=|{\cal U}|,\qquad
 Q=\binom n2,
\]

and \(\kappa\) is a proper \(n\)-edge-colouring of the bipartite
inclusion graph between \({\cal L}\) and \({\cal M}\).  Every
\(X\in{\cal M}\) has one missing colour \(\mu(X)\).  For
\(U\in{\cal U}\), the local pair map is

\[
 \psi_U:\binom U2\longrightarrow\binom{[n]}2,
\]

and

\[
 \ell(U)=Q-|\operatorname {im}\psi_U|,
 \qquad
 {\mathfrak L}(\kappa)=\sum_{U\in{\cal U}}\ell(U).
 \tag{0.1}
\]

The universal exact condition is

\[
                         \ell(U)=0\quad(U\in{\cal U}).
 \tag{0.2}
\]

The following strengthens the previously recorded odd-\(m\) obstruction.

### Theorem A (prime-admissibility and automatic resolution)

If (0.2) holds and \(m\ge2\), then

\[
                         \boxed{m+1\text{ is prime}.}
 \tag{0.3}
\]

For every colour \(c\), the missing-colour class

\[
                         {\cal E}_c=\{X:\mu(X)=c\}
 \tag{0.4}
\]

is not only a Steiner system \(S(m-1,m,2m)\): it is automatically closed
under set complementation.  Consequently it resolves into complementary
parallel pairs

\[
                         \{X,X^c\}.
 \tag{0.5}
\]

Thus universal local Latinness forces a large set of \(m+1\) resolvable
Steiner systems.  Condition (0.3) is only a divisibility condition; no
existence assertion is made when \(m+1\) is prime.

There is also an exact near version.  Suppose \(n=m+1\) is composite, let
\(p\) be a prime divisor of \(n\), and put

\[
                         T_{m,p}=\binom{m+p}{p-1}.
 \tag{0.6}
\]

### Theorem B (quantitative composite residue floor)

Every proper \(n\)-edge-colouring satisfies

\[
 \boxed{
 {\mathfrak L}(\kappa)\ge {N\over2T_{m,p}}.}
 \tag{0.7}
\]

In particular, choosing the least prime divisor of \(m+1\),

\[
 \boxed{
 { {\mathfrak L}(\kappa)\over QN}
 \ge {1\over2Q\binom{m+p}{p-1}}.}
 \tag{0.8}
\]

For odd \(m\ge3\), one may take \(p=2\), giving

\[
 {\mathfrak L}(\kappa)\ge {N\over2(m+2)},
 \qquad
 { {\mathfrak L}(\kappa)\over QN}
 \ge {1\over2Q(m+2)}.
 \tag{0.9}
\]

The normalized floor (0.8) tends to zero.  Hence this quantitative
divisibility argument does **not** give a non-\(o(1)\) obstruction to the
sufficient near-Latin target

\[
                         {\mathfrak L}(\kappa)=o(QN).
 \tag{0.10}
\]

Whether every proper colouring has a positive normalized defect bounded
away from zero requires a separate stability theorem; it is not settled
by the Steiner divisibility obstruction.

## 1. From universal pair maps to a large Steiner set

For completeness, first recall the exact implication.  For
\(U\in{\cal U}\) and \(c\in[n]\), put

\[
 r_c(U)=|\{a\in U:\mu(U\setminus\{a\})=c\}|.
 \tag{1.1}
\]

The local pair-to-point margin identity is

\[
                         \sum_{q\ni c}h_q(U)=n-r_c(U),
 \tag{1.2}
\]

where \(h_q(U)=|\psi_U^{-1}(q)|\).  If \(\psi_U\) is bijective, then
\(h_q(U)=1\) for every colour pair \(q\), and the left side of (1.2) is
\(n-1\).  Hence

\[
                         r_c(U)=1
 \tag{1.3}
\]

for every \(U,c\).

Thus adjacent middle sets, which are two facets of their common union
\(U\), have distinct missing colours.  The map

\[
                         \mu:{\cal M}\longrightarrow[n]
 \tag{1.4}
\]

is a proper \(n\)-colouring of \(J(2m,m)\).

Fix \(S\in{\cal L}\).  Its \(n\) extensions in \({\cal M}\) form a clique
of order \(n\), so their missing colours are all distinct.  Therefore,
for every \(c\), exactly one member of \({\cal E}_c\) contains \(S\).
This is precisely

\[
                         {\cal E}_c\cong S(m-1,m,2m).
 \tag{1.5}
\]

The \(n\) missing-colour classes partition \({\cal M}\), so they form a
large set of such systems.

The sign in (1.2) is worth auditing.  With

\[
 z_q(U)=h_q(U)-1,\qquad s_c(U)=r_c(U)-1,
\]

subtracting the \(n-1\) colour pairs incident with \(c\) gives

\[
                         \sum_{q\ni c}z_q(U)=-s_c(U).
 \tag{1.6}
\]

Thus the negative sign in the engine report is correct.

## 2. Complete divisibility classification

Let \({\cal D}\) be any Steiner system \(S(m-1,m,2m)\).  For an
\(i\)-set \(I\), the number of blocks containing \(I\) is forced to be

\[
 \lambda_i
 ={ \binom{2m-i}{m-1-i}\over\binom{m-i}{m-1-i}}
 \qquad(0\le i\le m-1).
 \tag{2.1}
\]

Put

\[
                         s=m-i.
\]

Then (2.1) becomes

\[
 \boxed{
 \lambda_{m-s}
 ={1\over s}\binom{m+s}{s-1}
 ={1\over m+1}\binom{m+s}s}
 \qquad(1\le s\le m).
 \tag{2.2}
\]

Consequently the complete elementary divisibility condition is

\[
 m+1\ \bigm|\ \binom{m+s}s
 \qquad(1\le s\le m).
 \tag{2.3}
\]

### Lemma 2.1 (prime iff all divisibilities hold)

For \(m\ge1\), all conditions in (2.3) hold if and only if \(m+1\) is
prime.

#### Proof

Put \(n=m+1\).  If \(n\) is prime and \(1\le s<n\), then

\[
 \binom{n-1+s}s
 ={n(n+1)\cdots(n+s-1)\over s!}
 \tag{2.4}
\]

is divisible by \(n\), because \(s!\) is prime to \(n\).

Conversely, suppose \(n\) is composite and let \(p\mid n\) be prime.
Then \(p<n\), so \(s=p\) is allowed.  If \(p^a\Vert n\), (2.4) gives

\[
 v_p\binom{n-1+p}p
 =v_p\!\left({n(n+1)\cdots(n+p-1)\over p!}\right)
 =a-1.
 \tag{2.5}
\]

Indeed, none of \(n+1,\ldots,n+p-1\) is divisible by \(p\), while
\(v_p(p!)=1\).  Thus \(n\nmid\binom{n-1+p}p\), contradicting (2.3).
\(\square\)

Theorem A's primality assertion follows from Lemma 2.1.

## 3. Every admissible Steiner class is complement-resolvable

Taking \(s=2\) in (2.2) gives

\[
                         \lambda_{m-2}={m+2\over2}.
 \tag{3.1}
\]

Thus every nontrivial system has even \(m\).  We now show that its
resolution is automatic.

Fix a block \(B\in{\cal D}\), and let \(d_0(B)\) be the number of blocks
disjoint from \(B\).  Inclusion-exclusion over the points of \(B\) gives

\[
 d_0(B)
 =\sum_{i=0}^{m}(-1)^i\binom mi\lambda_i,
 \tag{3.2}
\]

where \(\lambda_m=1\), since the unique block containing the \(m\)-set
\(B\) is \(B\) itself.  Using \(s=m-i\) and (2.2),

\[
 d_0(B)
 =(-1)^m+
 {1\over m+1}
 \sum_{s=1}^{m}(-1)^{m-s}
       \binom ms\binom{m+s}s.
 \tag{3.3}
\]

The elementary Chu--Vandermonde identity

\[
 \sum_{s=0}^{m}(-1)^s\binom ms\binom{m+s}s=(-1)^m
 \tag{3.4}
\]

implies

\[
 \sum_{s=0}^{m}(-1)^{m-s}\binom ms\binom{m+s}s=1.
 \tag{3.5}
\]

Substitution in (3.3) gives

\[
 d_0(B)
 =(-1)^m+{1-(-1)^m\over m+1}.
 \tag{3.6}
\]

Since \(m\) is even,

\[
                         d_0(B)=1.
 \tag{3.7}
\]

There is only one \(m\)-subset of \([2m]\) disjoint from \(B\), namely
\(B^c\).  Hence \(B^c\in{\cal D}\).  The blocks of \({\cal D}\) therefore
partition into complementary pairs, each pair being a parallel class on
\([2m]\).  This proves the resolution assertion in Theorem A.

## 4. A residue obstruction for approximate missing-colour designs

Return to an arbitrary proper edge-colouring \(\kappa\).  For a colour
\(c\) and \(S\in{\cal L}\), define

\[
 d_c(S)=|\{X\in{\cal M}:S\subset X,\ \mu(X)=c\}|.
 \tag{4.1}
\]

The ideal Steiner value is one.  Define its total lower-star defect by

\[
 {\mathfrak D}^-(\mu)
 =\sum_{c=1}^{n}\sum_{S\in{\cal L}}|d_c(S)-1|.
 \tag{4.2}
\]

Assume that \(p\mid n=m+1\) is prime.  Fix a colour \(c\) and a set

\[
                         I\in\binom{[2m]}{m-p}.
\]

Let \(e_c(I)\) be the number of members of \({\cal E}_c\) containing
\(I\).  Every such \(m\)-set has exactly \(p\) rank-\((m-1)\) facets
which contain \(I\).  Therefore

\[
 \sum_{\substack{S\in{\cal L}\\I\subset S}}
       (d_c(S)-1)
 =p\,e_c(I)-T_{m,p},
 \tag{4.3}
\]

where

\[
 T_{m,p}
 =|\{S\in{\cal L}:I\subset S\}|
 =\binom{m+p}{p-1}.
 \tag{4.4}
\]

Because \(m\equiv-1\pmod p\),

\[
 T_{m,p}
 =\binom{m+p}{p-1}
 \equiv1\pmod p.
 \tag{4.5}
\]

For example, in the product expression for (4.4), the \(p-1\) numerator
factors reduce to \(1,2,\ldots,p-1\), just as the denominator does.
Thus the integer in (4.3) is nonzero, and

\[
 \left|
 \sum_{S\supset I}(d_c(S)-1)
 \right|\ge1.
 \tag{4.6}
\]

Sum (4.6) over all \(I\).  Each \(S\) contains
\(\binom{m-1}{p-1}\) such sets.  The triangle inequality gives

\[
 \binom{2m}{m-p}
 \le
 \binom{m-1}{p-1}
 \sum_{S\in{\cal L}}|d_c(S)-1|.
 \tag{4.7}
\]

The exact factorial identity

\[
 { \binom{2m}{m-p}\over
   \binom{m-1}{p-1}}
 ={N\over\binom{m+p}{p-1}}
 ={N\over T_{m,p}}
 \tag{4.8}
\]

therefore yields

\[
 \sum_{S\in{\cal L}}|d_c(S)-1|
 \ge {N\over T_{m,p}}.
 \tag{4.9}
\]

Summing over all \(n\) colours,

\[
 \boxed{
 {\mathfrak D}^-(\mu)\ge {nN\over T_{m,p}}.}
 \tag{4.10}
\]

## 5. Transfer from missing-colour defect to pair-map defect

For a lower star \(S\), put

\[
 \sigma^-(S)=\sum_c(d_c(S)-1)_+
 ={1\over2}\sum_c|d_c(S)-1|,
 \tag{5.1}
\]

\[
 B^-(S)=\sum_c\binom{d_c(S)}2.
 \tag{5.2}
\]

Then

\[
                         B^-(S)\ge\sigma^-(S).
 \tag{5.3}
\]

For \(U\in{\cal U}\), retain

\[
 r_c(U)=|\{a\in U:\mu(U-a)=c\}|,
\]

\[
 \sigma^+(U)=\sum_c(r_c(U)-1)_+,
 \qquad
 B^+(U)=\sum_c\binom{r_c(U)}2.
 \tag{5.4}
\]

Every adjacent pair of middle sets has a unique intersection
\(S\in{\cal L}\) and a unique union \(U\in{\cal U}\).  Counting adjacent
pairs with equal missing colour in the two ways gives

\[
                         \sum_SB^-(S)=\sum_UB^+(U).
 \tag{5.5}
\]

The local pair-margin theorem gives

\[
                         \sigma^+(U)\le2\ell(U).
 \tag{5.6}
\]

Also, since \(r_c(U)\le n\),

\[
 \binom{r_c(U)}2
 \le {n\over2}(r_c(U)-1)_+.
\]

Consequently

\[
                         B^+(U)\le n\ell(U).
 \tag{5.7}
\]

Combining (5.1), (5.3), (5.5), and (5.7) gives

\[
 {1\over2}{\mathfrak D}^-(\mu)
 \le n{\mathfrak L}(\kappa).
 \tag{5.8}
\]

Now (4.10) proves

\[
                         {\mathfrak L}(\kappa)
 \ge {N\over2T_{m,p}},
\]

which is Theorem B.

The elementary bound (5.7) also sharpens the local collision estimate in
the engine report:

\[
 \boxed{
 B(U)=\sum_c\binom{r_c(U)}2\le n\,\ell(U).}
 \tag{5.9}
\]

It is stronger than the previously recorded
\((m^2-1)\ell(U)/2\) estimate for \(m\ge3\).

## 6. Audit of the local \(n=4\) countertable

The displayed \(n=4\) table in the engine report is locally legal.
Its four rows omit respectively colours \(1,2,3,4\), and the six pairs
of opposite entries are

\[
 (3,4),\ (2,1),\ (4,1),\ (3,2),\ (1,2),\ (4,3),
\]

so the two entries on every unordered local edge are distinct.  Its pair
images are

\[
 12\mapsto34,\quad
 13\mapsto12,\quad
 14\mapsto14,\quad
 23\mapsto23,\quad
 24\mapsto12,\quad
 34\mapsto34.
\]

Thus \(13,24\) are holes and \(12,34\) are double fibres.  The example
correctly proves that permutation-valued missing-colour margins do not
force \(\psi_U\) to be Latin.  It remains a local table, not a claimed
global colouring of \(H_3\).

## 7. Exact boundary

The universal target is now sharply obstructed:

\[
 \text{all }\psi_U\text{ bijective}
 \Longrightarrow
 \text{large set of resolvable }S(m-1,m,2m)
 \Longrightarrow
 m+1\text{ prime}.
\]

For composite \(m+1\), (0.7) is an unavoidable integral defect.  However,
its normalized size in (0.8) vanishes.  The proved estimate therefore
neither gives a positive limiting lower bound for
\({\mathfrak L}/(QN)\) nor contradicts the distinguished-pair sufficient
condition \({\mathfrak L}=o(QN)\).

The remaining alternatives are exact:

1. prove a stronger stability theorem giving
   \({\mathfrak L}\ge\varepsilon QN\) for some absolute
   \(\varepsilon>0\);
2. construct proper edge-colourings with
   \({\mathfrak L}=o(QN)\);
3. bypass average local Latinness and directly find one colour pair with
   \(o(W)\) upper holes and \(o(W/H)\) bichromatic cycles.

No one of these three alternatives is settled by Steiner divisibility.

# Uniform product-SCD tails after arbitrary Stage A

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom{2m+1}{m},\qquad
 B=\frac{W}{2m+1}=\operatorname{Cat}_m .
\]

There is a completely factor-blind literal word which covers all ranks at
distance more than \(H\) from the two middle ranks. Its exact length is

\[
 2L_m(m-H-1),
\]

where

\[
 \boxed{
 L_m(r)=2\sum_{a=0}^{\lfloor m/2\rfloor}
 \left(\binom ma-\binom m{a-1}\right)w_m(a)C_m(r-a)}
 \tag{0.1}
\]

with

\[
 w_m(0)=m,\qquad w_m(a)=m-2a+1\quad(a>0),
 \tag{0.2}
\]

and

\[
 C_m(t)=
 \begin{cases}
 0,&t<0,\\
 \displaystyle\binom m{\min(t,\lfloor m/2\rfloor)},&t\ge0.
 \end{cases}
 \tag{0.3}
\]

The first factor \(2\) in this statement is the odd-dimensional trimmed
lift. The factor \(2\) already present in (0.1) is the sum of the two sides
of each product-chain gadget. There is no further factor for the second
tail: the same even word covers both tails.

There is an absolute constant \(C\) such that, for every \(m\ge1\) and
\(0\le H\le m-1\),

\[
 \boxed{
 \frac{2L_m(m-H-1)}{\binom{2m+1}{m}}
 \le C\exp\!\left(-\frac{H^2}{8m}\right).}
 \tag{0.4}
\]

Consequently

\[
 \frac{H}{\sqrt m}\longrightarrow\infty
 \quad\Longrightarrow\quad
 2L_m(m-H-1)=o(W),
 \tag{0.5}
\]

uniformly, with no hypothesis \(H\le m/2\). The scale in (0.5) is sharp
for this explicit product-SCD word.

The tail may be concatenated after **any** literal Stage-A word. It uses no
MSW chronology, exact-factor ownership, port alignment, common owner,
endpoint matching, or seam safety. Every even-dimensional witness lies
inside one product gadget. After the odd trimmed lift, a witness may cross
the lift's internal \(Q\mid\{z\}\) seam, but every tail witness remains
inside the tail block and never uses the Stage-A/tail seam. Concatenation
therefore preserves every old witness.

The datum not supplied by the tail theorem is entirely central. A
seam-free black-box sufficient interface is that the targets left inside

\[
 \mathcal B_{m,H}:=
 \bigcup_{j=m-H}^{m+H+1}\binom{[2m+1]}j
 \tag{0.6}
\]

admit an \(o(W)\)-length literal repair word. The simpler condition that
their number is \(o(W)\) is a uniform sufficient certificate, since one
may append each target as one literal letter. Neither condition is claimed
necessary for a redesigned Stage A or for a construction deliberately
using cross-seam witnesses.

For the standard row-linearized Stage A, define

\[
 J_H(F):=\sum_{q=1}^H\frac{O_q(F)}{c_q},
 \qquad
 c_q=\left\lfloor
 \frac{W}{\binom{2m+1}{m-q}}
 \right\rfloor .
 \tag{0.7}
\]

If \(F\) is any exact factor satisfying \(J_H(F)=o(W)\), and \(R\)
complete cyclic rows are deleted, then the central repair charge is at
most

\[
 2J_H(F)+2nR(1+S_H),
 \qquad
 S_H:=\sum_{q=1}^H\frac1{c_q}=O(\sqrt m)
 \tag{0.8}
\]

uniformly for every \(H\le m\). Thus

\[
 R=o(B/\sqrt m)
 \tag{0.9}
\]

is a factor-independent sufficient row-leave rate. The same rate preserves
\(J_H=o(W)\) under arbitrary exact row replacements.

Combining (0.4), (0.8), and the exact row collar proves:

\[
 \boxed{
 \sqrt m\ll H\ll m,\quad
 J_H(F)=o(W),\quad
 R=o(B/\sqrt m)
 \ \Longrightarrow\
 \nu(2m+1)\le W+o(W).}
 \tag{0.10}
\]

This is uniform over all exact factors meeting the displayed central
condition. Exactness by itself is not enough to imply the standard
row-shadow condition \(J_H=o(W)\): the canonical MSW exact factor has at
least

\[
 (m-3)\operatorname{Cat}_{m-2}-\frac{2W}{m+2}
 =\left(\frac1{32}-o(1)\right)W
 \tag{0.11}
\]

missing rank-\((m-1)\) targets. Also, saying that an \(o(W)\) number of
*rows* is deleted is vacuous, because the whole factor has only
\(B=W/n=o(W)\) rows.

## 1. Exact even-dimensional product word

Split a \(2m\)-set as \(X\sqcup Y\), with \(|X|=|Y|=m\), and fix arbitrary
symmetric-chain decompositions of \(2^X\) and \(2^Y\).

For completeness, such a decomposition exists by induction. From every
chain
\[
 C_a\subset\cdots\subset C_{m-a}
\]
in \(2^{[m]}\), adjoining a new coordinate \(z\) produces the symmetric
chain
\[
 C_a\subset\cdots\subset C_{m-a}
 \subset C_{m-a}\cup\{z\},
\]
and, when nonempty, the second symmetric chain
\[
 C_a\cup\{z\}\subset\cdots\subset C_{m-a-1}\cup\{z\}.
\]
These chains are saturated, pairwise disjoint, and partition
\(2^{[m+1]}\).

A symmetric chain of minimum rank \(a\) has the form

\[
 C_a\subset C_{a+1}\subset\cdots\subset C_{m-a},
 \qquad |C_j|=j.
 \tag{1.1}
\]

Write \(C_j\setminus C_{j-1}=\{e_j\}\). Define its forward increment word

\[
 R(C)=
 \begin{cases}
 \{e_1\},\ldots,\{e_m\},&a=0,\\
 C_a,\{e_{a+1}\},\ldots,\{e_{m-a}\},&a>0,
 \end{cases}
 \tag{1.2}
\]

and \(L(C)=\operatorname{rev}R(C)\). Every entry is nonempty and

\[
 |L(C)|=|R(C)|=w_m(a).
 \tag{1.3}
\]

Every nonempty member of \(C\) is the union of a prefix of \(R(C)\) and
the union of a suffix of \(L(C)\). The omission of the empty initial
member of the unique \(a=0\) chain explains \(w_m(0)=m\), rather than
\(m+1\).

The number of chains with minimum rank \(a\) is

\[
 A_m(a):=\binom ma-\binom m{a-1}.
 \tag{1.4}
\]

Indeed, every symmetric chain whose minimum rank is at most \(a\) contains
exactly one rank-\(a\) member. Hence the number of such chains is
\(\binom ma\), and subtraction at consecutive ranks gives (1.4).

For every ordered pair \((C,D)\) of half-cube chains, with minimum ranks
\(a,b\) satisfying

\[
 a+b\le r,
 \tag{1.5}
\]

append the gadget

\[
 L(C)\mathbin\Vert R(D).
 \tag{1.6}
\]

Concatenate all these gadgets in an arbitrary order.

### Theorem 1.1 (literal simultaneous two-tail coverage)

The word (1.6), over all pairs satisfying (1.5), covers every nonempty
\(S\subseteq X\sqcup Y\) for which

\[
 |S|\le r
 \quad\text{or}\quad
 |S|\ge2m-r.
 \tag{1.7}
\]

Its exact constructed length is \(L_m(r)\) from (0.1).

#### Proof

Write \(S=S_X\sqcup S_Y\), and let \(C,D\) be the unique half-chains
containing \(S_X,S_Y\), with minimum ranks \(a,b\).

If \(|S|\le r\), then

\[
 a+b\le |S_X|+|S_Y|=|S|\le r.
 \tag{1.8}
\]

If \(|S|\ge2m-r\), symmetry of the chains gives

\[
 a\le m-|S_X|,\qquad b\le m-|S_Y|,
\]

and hence

\[
 a+b\le2m-|S|\le r.
 \tag{1.9}
\]

Thus the relevant pair is present. A suffix of \(L(C)\) has union \(S_X\)
and a prefix of \(R(D)\) has union \(S_Y\); their concatenation is one
contiguous interval of (1.6) with union \(S\). If one part is empty, use
only the other side. This proves both tails directly, without applying
complementation to an OR witness.

The length is

\[
 \sum_{a+b\le r}A_m(a)A_m(b)
 \bigl(w_m(a)+w_m(b)\bigr).
 \tag{1.10}
\]

The two summands are equal after interchanging the halves, while

\[
 \sum_{b=0}^{\min(t,\lfloor m/2\rfloor)}A_m(b)
 =\binom m{\min(t,\lfloor m/2\rfloor)}
 \tag{1.11}
\]

for \(t\ge0\), with value zero for \(t<0\). Equations (1.10)--(1.11)
give exactly (0.1). \(\square\)

Every witness in Theorem 1.1 lies inside one gadget. Therefore the order
of the gadgets and every inter-gadget seam are irrelevant.

## 2. Exact odd-dimensional trimmed lift

### Lemma 2.1 (trimmed lift)

Let \(Q=(Q_1,\ldots,Q_N)\) be any nonempty set-valued word on a ground set
\(V\), and suppose it covers a family \(\mathcal F\) of nonempty targets.
For a new coordinate \(z\), the word

\[
 Q_1,\ldots,Q_N,\{z\},
 Q_1\cup\{z\},\ldots,Q_{N-1}\cup\{z\}
 \tag{2.1}
\]

has exactly \(2N\) entries and covers

\[
 \mathcal F\cup\{\{z\}\}
 \cup\{S\cup\{z\}:S\in\mathcal F\}.
 \tag{2.2}
\]

#### Proof

The first copy preserves all old witnesses, and \(\{z\}\) is explicit.
If \(Q_i,\ldots,Q_j\) witnesses \(S\) and \(j<N\), use the corresponding
interval in the transformed copy. If \(j=N\), use instead

\[
 Q_i,\ldots,Q_N,\{z\}.
\]

Its union is \(S\cup\{z\}\). This last seam witness is exactly why the
final transformed entry may be omitted. \(\square\)

Apply Lemma 2.1 to the word of Theorem 1.1. It has length \(2L_m(r)\) and
covers all nonempty subsets of a \((2m+1)\)-set with

\[
 |T|\le r
 \quad\text{or}\quad
 |T|\ge2m-r+1.
 \tag{2.3}
\]

Putting \(r=m-H-1\), these are precisely

\[
 |T|\le m-H-1
 \quad\text{or}\quad
 |T|\ge m+H+2.
 \tag{2.4}
\]

Equivalently, all depths \(q\ge H+1\) on both sides of the middle are
covered, and Stage A is responsible exactly for the rank band (0.6).
There is no missing parity layer at \(q=H+1\).

## 3. Uniform tail estimate and its sharp scale

Put

\[
 h=\lfloor m/2\rfloor,\qquad
 \epsilon=m-2h\in\{0,1\},\qquad
 P_m=\binom mh,
\]

\[
 x=h-a,\qquad d=H+1-\epsilon.
\tag{3.1}
\]

For \(0\le x<h\), direct subtraction in (1.4) gives the exact weight

\[
 D_{m,x}:=A_m(h-x)w_m(h-x)
 =\binom m{h-x}
 \frac{(2x+\epsilon+1)^2}{h+x+\epsilon+1}.
 \tag{3.2}
\]

At the exceptional value \(x=h\), corresponding to \(a=0\),

\[
 D_{m,h}=m.
 \tag{3.3}
\]

The exact parity-uniform form of (0.1) is

\[
 L_m(m-H-1)
 =2\sum_{x=0}^{h}D_{m,x}
 \binom m{h-(d-x)_+},
 \tag{3.4}
\]

with a binomial having negative lower index interpreted as zero. Moreover,

\[
 \sum_{x=0}^{h}D_{m,x}=2^m-1,
 \tag{3.5}
\]

because the increment words enumerate all nonempty members of all
half-cube chains.

The elementary central-ratio inequality is

\[
 \frac{\binom m{h-y}}{P_m}\le e^{-y^2/m}
 \qquad(0\le y\le h).
 \tag{3.6}
\]

For even \(m=2h\), the ratio is

\[
 \prod_{j=1}^{y}\frac{h-j+1}{h+j};
\]

for odd \(m=2h+1\), it is

\[
 \prod_{j=1}^{y}\frac{h-j+1}{h+j+1}.
\]

Using \(\log(1-u)\le-u\) proves (3.6). Combining (3.2) and (3.6) gives

\[
 \frac{D_{m,x}}{P_m}
 \le \frac{8(x+1)^2}{m}e^{-x^2/m}
 \qquad(x<h).
 \tag{3.7}
\]

Split (3.4) at \(t=\lfloor d/2\rfloor\). If \(x\le t\), then
\((d-x)_+\ge H/2\), so (3.6) bounds the second binomial by

\[
 P_m e^{-H^2/(4m)}.
\]

Using (3.5), this part of (3.4), divided by \(\binom{2m}{m}\), is at most

\[
 2\frac{2^mP_m}{\binom{2m}{m}}e^{-H^2/(4m)}.
 \tag{3.8}
\]

If \(x>t\), then \(x>H/2\), and

\[
 e^{-x^2/m}
 \le e^{-H^2/(8m)}e^{-x^2/(2m)}.
\]

Equations (3.4) and (3.7) bound the nonexceptional part, after
normalization, by

\[
 16\frac{P_m^2}{\binom{2m}{m}}
 e^{-H^2/(8m)}
 \left[
 \frac1m\sum_{x\ge0}(x+1)^2e^{-x^2/(2m)}
 \right].
 \tag{3.9}
\]

The bracket is \(O(\sqrt m)\). Wallis' inequalities give uniformly

\[
 \frac{2^mP_m}{\binom{2m}{m}}=O(1),
 \qquad
 \frac{P_m^2\sqrt m}{\binom{2m}{m}}=O(1).
 \tag{3.10}
\]

The exceptional \(x=h\) contribution is
\(O(m2^{-m})\), which is also
\(O(e^{-H^2/(8m)})\) for \(H\le m-1\). Enlarging one absolute constant
for the smallest \(m\) proves

\[
 \frac{L_m(m-H-1)}{\binom{2m}{m}}
 \le C e^{-H^2/(8m)}.
 \tag{3.11}
\]

Finally,

\[
 \binom{2m+1}{m}
 =\frac{2m+1}{m+1}\binom{2m}{m},
\]

so (3.11) proves (0.4).

No moderate-deviation upper range is used. In particular, \(H=o(m^{2/3})\)
and \(H\le m/2\) are not tail hypotheses. If \(H\ge m\), the outer family
is empty and the tail charge may be zero.

For completeness, the threshold is sharp for this particular construction.
If \(H/\sqrt m\to c<\infty\), then

\[
 \frac{L_m(m-H-1)}{\binom{2m}{m}}\longrightarrow T(c)>0,
 \tag{3.12}
\]

where

\[
 \begin{aligned}
 T(c)={}&4\left(c^2+\frac12\right)e^{-c^2}\operatorname{erf}(c)
 +\frac{4c}{\sqrt\pi}e^{-2c^2}\\
 &+2\sqrt2\,\operatorname{erfc}(\sqrt2c).
 \end{aligned}
 \tag{3.13}
\]

This follows from (3.4) by the mesh
\(u=(2x+\epsilon)/\sqrt m\), dominated convergence using (3.7), and
the integral

\[
 \frac4{\sqrt\pi}\left[
 \int_0^{2c}u^2e^{-[u^2+(2c-u)^2]/2}\,du+
 \int_{2c}^{\infty}u^2e^{-u^2/2}\,du
 \right].
 \tag{3.14}
\]

Thus \(H/\sqrt m\to\infty\) is necessary and sufficient for this
product-SCD word to have \(o(W)\) length. This is not a lower bound for
all possible tail constructions.

## 4. The exact black-box Stage-A interface

For a literal word \(U\), let \(\operatorname{Cov}(U)\) be its family of
contiguous interval unions. Concatenation is monotone:

\[
 \operatorname{Cov}(U)\cup\operatorname{Cov}(V)
 \subseteq\operatorname{Cov}(U\Vert V).
 \tag{4.1}
\]

Indeed, every interval internal to either block remains an interval after
concatenation. Cross-seam intervals may create extra targets but cannot
remove a witness.

### Theorem 4.1 (factor-blind composition)

Let \(0\le H\le m-1\). Let \(A_{m,H}\) be any literal word on
\([2m+1]\), and let
\(\mathcal E_{m,H}\subseteq\mathcal B_{m,H}\) be the targets it does not
cover. Then

\[
 \boxed{
 \nu(2m+1)\le
 |A_{m,H}|+|\mathcal E_{m,H}|+2L_m(m-H-1).}
 \tag{4.2}
\]

More generally, if \(R_{m,H}\) is any literal word covering
\(\mathcal E_{m,H}\), then

\[
 \boxed{
 \nu(2m+1)\le
 |A_{m,H}|+|R_{m,H}|+2L_m(m-H-1).}
 \tag{4.3}
\]

#### Proof

For (4.2), concatenate \(A_{m,H}\), one set-letter equal to each target in
\(\mathcal E_{m,H}\), and the odd tail word of Section 2. For (4.3), use
\(R_{m,H}\) in place of the singleton repairs. The first two blocks cover
the central band and the last covers its complement. Equation (4.1)
preserves every internal witness. \(\square\)

Therefore, if

\[
 |A_{m,H}|\le W+o(W),\qquad
 |\mathcal E_{m,H}|=o(W),\qquad
 H/\sqrt m\to\infty,
 \tag{4.4}
\]

then \(\nu(2m+1)\le W+o(W)\). A stand-alone repair word of length \(o(W)\)
is the exact modular hypothesis used by this seam-free concatenation
argument; the cardinal condition in (4.4) is a direct completely
structure-free certificate. Neither is asserted necessary for a joint
construction which exploits cross-block intervals.

This theorem remains valid after an arbitrary exact factor is switched,
conjugated, replaced, partially deleted, or abandoned entirely. The only
input to the theorem is the literal coverage of the resulting Stage-A
word.

## 5. Standard central compiler for an arbitrary exact factor

Let \(F\) be any family of cyclic orders of \([n]\). For a row \(\pi\),
write \(I_\pi(j,s)\) for the cyclic interval of length \(s\) beginning at
position \(j\), and put

\[
 E_j=I_\pi(j,m-H).
\]

Emit the row block

\[
 E_0,E_1,\ldots,E_{n-1},E_0,E_1,\ldots,E_{2H}.
 \tag{5.1}
\]

It has \(n+2H+1\) entries and

\[
 \bigcup_{u=0}^{t-1}E_{j+u}
 =I_\pi(j,m-H+t-1)
 \quad(1\le t\le2H+2).
 \tag{5.2}
\]

For \(0\le q\le H\), define the lower-depth histogram

\[
 \mu_q^F(S)=
 \#\{(\pi,j):\pi\in F,\ I_\pi(j,m-q)=S\},
 \tag{5.3}
\]

and the number of lower holes

\[
 M_q(F)=
 \#\left\{S\in\binom{[n]}{m-q}:\mu_q^F(S)=0\right\}.
 \tag{5.4}
\]

Complementation sends every retained lower interval to a retained upper
interval:

\[
 [n]\setminus I_\pi(j,m-q)
 =I_\pi(j+m-q,m+1+q).
 \tag{5.5}
\]

Hence the upper rank \(m+1+q\) has exactly \(M_q(F)\) holes as well.
If \(F\) has \(K\) rows, the row blocks plus literal hole repairs cover
the central band in length

\[
 K(n+2H+1)+2\sum_{q=0}^HM_q(F).
 \tag{5.6}
\]

If \(F\) is an exact middle factor, then \(K=B\),
\(\mu_0^F\equiv1\), and \(M_0(F)=0\). Thus

\[
 \boxed{
 \nu(2m+1)\le
 W+\frac{2H+1}{n}W+
 2\sum_{q=1}^HM_q(F)+
 2L_m(m-H-1).}
 \tag{5.7}
\]

This finite inequality holds for every exact factor; it contains no MSW
hypothesis.

For \(q\ge1\), put

\[
 N_q=\binom n{m-q},\qquad
 c_q=\left\lfloor\frac W{N_q}\right\rfloor.
 \tag{5.8}
\]

A balanced quota \(b_q\) takes values in \(\{c_q,c_q+1\}\) and has total
mass \(W\). Define

\[
 O_q(F)=\min_{b_q}
 \sum_S\bigl(\mu_q^F(S)-b_q(S)\bigr)_+.
 \tag{5.9}
\]

Since \(\mu_q^F\) and \(b_q\) have the same total mass, total overload
equals total underload. Every hole contributes at least \(c_q\) to the
underload, so

\[
 M_q(F)\le\frac{O_q(F)}{c_q}.
 \tag{5.10}
\]

Consequently (5.7) implies

\[
 \nu(2m+1)\le
 W+\frac{2H+1}{n}W+
 2J_H(F)+2L_m(m-H-1).
 \tag{5.11}
\]

Thus an arbitrary modified exact factor composes with the tail whenever
its own \(J_H\) is \(o(W)\). The tail does not prove that central
hypothesis.

## 6. Uniform floor-buffer theorem for deleted leaves

The next point is the decisive improvement over the crude estimate which
charges every deleted occurrence once at every depth.

### Lemma 6.1 (floor-buffer deletion)

Let \(\mu\) be a nonnegative integral vector of total mass \(W\), let
\(b\in\{c,c+1\}^{\mathcal X}\) have total mass \(W\), and let
\(0\le\delta\le\mu\) be any deleted occurrence vector. Put
\(\mu'=\mu-\delta\). Then

\[
 \boxed{
 c\,|\{S:\mu'(S)=0\}|
 \le\sum_S(b(S)-\mu(S))_++\|\delta\|_1.}
 \tag{6.1}
\]

#### Proof

If \(\mu'(S)=0\), then \(\mu(S)=\delta(S)\). Since \(b(S)\ge c\),

\[
 c\le b(S)
 \le(b(S)-\mu(S))_++\mu(S)
 =(b(S)-\mu(S))_++\delta(S).
 \tag{6.2}
\]

Sum over the holes, enlarge the underload sum to all coordinates, and
bound the deleted mass by \(\|\delta\|_1\). \(\square\)

### Lemma 6.2 (uniform reciprocal capacity)

For every \(1\le H\le m\),

\[
 \boxed{
 S_H:=\sum_{q=1}^H\frac1{c_q}=O(\sqrt m)}
 \tag{6.3}
\]

with an absolute implied constant.

#### Proof

For every \(x\ge1\),

\[
 \frac1{\lfloor x\rfloor}\le\frac2x.
\]

Therefore

\[
 \frac1{c_q}\le\frac{2N_q}{W}.
 \tag{6.4}
\]

The exact ratio is

\[
 \frac{N_q}{W}
 =\prod_{i=0}^{q-1}\frac{m-i}{m+2+i}.
 \tag{6.5}
\]

Since

\[
 \log\frac{m-i}{m+2+i}
 \le-\frac{2i+2}{2m+1},
\]

we obtain

\[
 \frac{N_q}{W}
 \le\exp\!\left(-\frac{q(q+1)}{2m+1}\right).
 \tag{6.6}
\]

Equations (6.4)--(6.6), followed by comparison with a Gaussian integral,
give (6.3). \(\square\)

An alternative exact summation, useful as a check, is

\[
 S_H\le
 \frac2W\sum_{q=1}^mN_q
 =2\frac{2^{2m}-W}{W}
 =O(\sqrt m).
 \tag{6.7}
\]

The last equality is the central-binomial estimate. Both derivations are
uniform in \(H\).

Now let \(F\) be an exact factor and delete an arbitrary family
\(\mathcal D\) of \(R\) whole cyclic rows. Put \(P=F\setminus\mathcal D\).
At every depth \(q\), the deleted histogram has total mass \(nR\).
Lemma 6.1, applied to a minimizing quota in (5.9), gives

\[
 M_q(P)\le\frac{O_q(F)+nR}{c_q}
 \qquad(1\le q\le H).
 \tag{6.8}
\]

At \(q=0\), exactness gives the identity

\[
 M_0(P)=nR.
 \tag{6.9}
\]

Therefore

\[
 \boxed{
 \sum_{q=0}^HM_q(P)
 \le J_H(F)+nR(1+S_H).}
 \tag{6.10}
\]

### Theorem 6.3 (exact arbitrary-factor leave interface)

For every exact factor \(F\), every deletion of \(R\) complete rows, and
every \(0\le H\le m-1\),

\[
 \boxed{\begin{aligned}
 \nu(2m+1)\le{}&
 (B-R)(n+2H+1)\\
 &+2J_H(F)+2nR(1+S_H)\\
 &+2L_m(m-H-1).
 \end{aligned}}
 \tag{6.11}
\]

All terms are integral except the displayed upper bounds involving
\(J_H/c_q\); the constructed word itself consists only of the retained
integral row blocks, literal target repairs, and the integral tail
gadgets.

In particular, for one absolute \(C_0\),

\[
 \boxed{
 \nu(2m+1)\le
 W+\frac{2H+1}{n}W+
 2J_H(F)+C_0nR\sqrt m+
 2L_m(m-H-1).}
 \tag{6.12}
\]

Hence, uniformly over arbitrary sequences \(F_m,H_m,R_m\),

\[
 \frac{H_m}{\sqrt m}\to\infty,\qquad
 H_m=o(m),\qquad
 J_{H_m}(F_m)=o(W),\qquad
 R_m=o(B/\sqrt m)
 \tag{6.13}
\]

imply \(\nu(2m+1)\le W+o(W)\).

In middle-occurrence units \(\Lambda=nR\), the row-leave hypothesis is

\[
 \Lambda=o(W/\sqrt m).
 \tag{6.14}
\]

For a general depth-dependent occurrence leave \(\delta_q\), the same
proof replaces (6.14) by the weighted sufficient condition

\[
 \sum_{q=1}^H\frac{\|\delta_q\|_1}{c_q}=o(W),
 \tag{6.15}
\]

together with an \(o(W)\) rank-\(m\) leave and an \(W+o(W)\)-length
realization of the retained Stage-A structure.

## 7. Stability under exact modifications

Suppose \(F'\) is obtained from \(F\) by replacing at most \(R\) rows and
is again exact. Then, at every depth,

\[
 \|\mu_q^{F'}-\mu_q^F\|_1\le2nR.
 \tag{7.1}
\]

For equal-mass histograms,

\[
 O_q(F)=\frac12\min_{b_q}\|\mu_q^F-b_q\|_1.
 \tag{7.2}
\]

Distance to a fixed set is one-Lipschitz, so (7.1)--(7.2) give

\[
 |O_q(F')-O_q(F)|\le nR.
 \tag{7.3}
\]

Consequently

\[
 \boxed{
 J_H(F')\le J_H(F)+nRS_H.}
 \tag{7.4}
\]

Thus \(R=o(B/\sqrt m)\) preserves \(J_H=o(W)\), regardless of which
replacement rows are chosen. This is the promised history-free
modification theorem. For larger or non-rowwise modifications, the tail
still composes, but one must verify the resulting central repair profile
directly.

## 8. Exact obstruction and implication boundary

### 8.1 Exactness alone does not control Stage A

The proved MSW fixed-hole theorem gives

\[
 M_1(F_m^{\mathrm{MSW}})
 \ge
 (m-3)\operatorname{Cat}_{m-2}-\frac{2W}{m+2}
 =\left(\frac1{32}-o(1)\right)W.
 \tag{8.1}
\]

Therefore

\[
 \text{exact factor}\not\Longrightarrow
 \sum_{q\le H}M_q=o(W)
\]

even with zero deleted rows. This counterexample concerns the standard
factor-shadow hole ledger. It does not rule out a different nonlinear
word which compresses some of those missing targets.

### 8.2 “An \(o(W)\) row leave” is vacuous

The whole exact factor contains only

\[
 B=\frac W{2m+1}=o(W)
\]

rows. Deleting every row is therefore an \(o(W)\)-sized leave if the unit
is “rows,” yet it leaves all \(W\) middle targets uncovered. The natural
row normalization is \(B\), not \(W\).

If leave size means middle occurrences, \(\Lambda=o(W)\) repairs the
middle layer itself at \(o(W)\) cost but does not, without a profile
theorem, control the simultaneous losses at the other \(H\) depths. The
uniform floor-buffer certificate is the stronger
\(\Lambda\sqrt m=o(W)\), or the exact weighted ledger (6.15). No necessity
of this sufficient rate is claimed: a structured larger leave may be
harmless if its actual central target or repair profile is \(o(W)\).

### 8.3 Precise proved and unproved statements

The following are proved.

1. The product-SCD tail covers every depth \(q\ge H+1\) on both sides,
   literally and integrally, at the exact charge \(2L_m(m-H-1)\).
2. Its charge is \(o(W)\) uniformly whenever
   \(H/\sqrt m\to\infty\); no \(H\le m/2\) or
   \(H=o(m^{2/3})\) restriction is needed.
3. The tail has no interface condition with Stage A.
4. Any \(W+o(W)\)-length Stage-A word whose residual central family has
   an \(o(W)\)-length repair word composes to coefficient one.
5. For standard row linearization, \(J_H=o(W)\) plus deletion of
   \(o(B/\sqrt m)\) arbitrary rows is a uniform sufficient certificate.
6. The same rate protects \(J_H=o(W)\) under arbitrary exact row
   replacements.

The following are not proved and must not be inferred.

1. Arbitrary exactness does not imply \(J_H=o(W)\) or \(o(W)\) central
   holes.
2. No implication from an \(o(W)\) leave measured in components, owners,
   or unweighted occurrences to an \(o(W)\) central repair family is
   proved here. For rows the statement is explicitly false by Section
   8.2; for occurrence leaves the proved substitute is the weighted
   condition (6.15).
3. The rate \(o(B/\sqrt m)\) is sufficient, not asserted necessary.
4. The tail theorem supplies no MWB, synchronization, owner assignment,
   or exact-factor completion.
5. The condition \(H=o(m)\) belongs only to the standard central row
   collar \((2H+1)W/n\); it is not a tail hypothesis.

## 9. Independent audit of the decisive steps

1. **Two factors of two.** Equation (1.10) produces the factor \(2\) in
   \(L_m\) by exchanging the two half-cubes. Lemma 2.1 then doubles the
   even word. The same even gadgets already cover both tails, so there is
   no third doubling.
2. **Upper-tail legality.** Inequality (1.9) schedules the same chain pair
   for an upper target, and the upper chain members are still unions of
   the displayed increment intervals. No complement of an OR witness is
   taken.
3. **Odd endpoint.** If an old witness reaches the last entry, the
   first-copy suffix followed by \(\{z\}\) replaces the deleted final
   transformed letter. Hence the lift length is exactly \(2L_m\), not
   \(2L_m+1\).
4. **Rank boundary.** With \(r=m-H-1\), the odd upper threshold is
   \(2m-r+1=m+H+2\). Thus Stage A stops at \(m+H+1\), with no uncovered
   interface layer.
5. **Uniformity.** The split in (3.8)--(3.9) treats all
   \(0\le H\le m-1\), including \(H>m/2\). The exponential is therefore
   a uniform sequence bound, not a fixed-\(A\) statement.
6. **Deletion mass.** A deleted cyclic row removes exactly \(n\)
   occurrences at every depth. At \(q=0\), exactness makes all \(nR\)
   removed middle targets distinct. At \(q\ge1\), Lemma 6.1 uses the
   floor \(c_q\) before declaring a new hole.
7. **Capacity sum.** Both the Gaussian ratio proof (6.4)--(6.6) and the
   exact half-cube sum (6.7) give \(S_H=O(\sqrt m)\), independently.
8. **Modification constant.** Replacing \(R\) rows changes the histogram
   by \(L^1\)-distance at most \(2nR\). The factor \(1/2\) in (7.2) yields
   the exact overload perturbation \(nR\), not \(2nR\).
9. **MSW constant.** The certified obstruction is \(1/32-o(1)\), not
   \(1/16-o(1)\).

The uniform product-SCD tail gate is therefore closed. In this modular
route, the remaining condition is a central Stage-A repair theorem, with
(6.13) giving one fully quantified arbitrary-factor/leave interface.

Independent supporting audits are recorded in
MATH_AUDIT_N_PRODUCT_SCD_TWO_TAIL_INTERFACE_20260726.md,
MATH_ATTACK_N_PRODUCT_SCD_TAIL_UNIFORM_ASYMPTOTIC_20260726.md, and
MATH_AUDIT_N_PRODUCT_SCD_STAGEA_LEAVE_INTERFACE_20260726.md.

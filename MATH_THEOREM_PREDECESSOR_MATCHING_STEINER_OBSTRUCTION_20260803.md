# Predecessor matchings with locally simple upper-colour classes force punctured Steiner systems

## Scope and outcome

Let

\[
X=[2m-1],\qquad
\mathcal L=\binom{X}{m-1},\qquad
\mathcal M=\binom{X}{m},
\]

and let \(M_0:\mathcal L\to\mathcal M\) be a perfect containment
matching. Thus

\[
L\subset M_0(L)
\]

for every \(L\in\mathcal L\), and every member of \(\mathcal M\) is
used once.

For \(V\in\mathcal M\), write

\[
q(V)=M_0^{-1}(V),\qquad a(V)=V\setminus q(V).
\]

Thus \(a(V)\) is the unique coordinate added by the matching edge
\(q(V)\subset V\).

For every upper colour \(R\in\binom{X}{m+1}\), define

\[
f_R:R\longrightarrow R,
\qquad
f_R(x)=a(R\setminus\{x\}).
\tag{1}
\]

The strong local-simplicity ansatz asks that every \(f_R\) be a
permutation. The main result of this note is:

> **Theorem.** If every map \(f_R\) is a permutation, then for every
> coordinate \(y\in X\) there is a Steiner system
> \[
> S(m-2,m-1,2m-2).
> \]
> Consequently, the standard divisibility conditions force \(m\) to
> be prime. In particular, the ansatz is impossible at \(k=17\), where
> \(m=9\), and at every odd dimension \(k=2m-1\) with composite \(m\).

This is an obstruction to the strong **all-rooted-occurrences are
tail/head-simple** ansatz. It is not an obstruction to a Hamilton
selector using a smaller or more complicated occurrence family, and
it is not an obstruction to \(\nu(k)=B(k)\).

## 1. Exact relation with colour--tail--head occurrences

Fix \(R\in\binom{X}{m+1}\) and \(x\in R\). Put

\[
T_{R,x}=R\setminus\{x\},
\qquad
Q_{R,x}=q(T_{R,x}).
\]

Since \(a(T_{R,x})=f_R(x)\),

\[
Q_{R,x}=R\setminus\{x,f_R(x)\}.
\]

The other middle set in \(R\) containing this lower colour is

\[
H_{R,x}=Q_{R,x}\cup\{x\}
       =R\setminus\{f_R(x)\}.
\tag{2}
\]

Thus the rooted occurrence of upper colour \(R\) is the directed edge

\[
e_{R,x}:T_{R,x}\longrightarrow H_{R,x}.
\tag{3}
\]

The tails \(T_{R,x}\) are automatically all distinct. The heads
\(H_{R,x}\) are all distinct if and only if \(f_R\) is injective, hence
if and only if \(f_R\) is a permutation. Also

\[
f_R(x)\in R\setminus\{x\},
\]

so every permutation \(f_R\) obtained in this way is automatically a
derangement and no edge (3) is a loop.

Therefore the permutation condition is exactly the assertion that the
entire rooted occurrence class of each fixed upper colour is both
tail-simple and head-simple. It does **not** by itself select a global
successor permutation or prove that the selected occurrence graph is
connected.

### 1.1. Every predecessor matching has a balanced fractional selector

There is no corresponding fractional obstruction. Form the
three-partite occurrence hypergraph with parts

\[
\binom X{m+1}_{\rm colour},\qquad
\binom Xm_{\rm tail},\qquad
\binom Xm_{\rm head},
\]

and hyperedges

\[
(R,T_{R,x},H_{R,x})
\qquad
(R\in\tbinom X{m+1},\ x\in R).
\]

Assign every hyperedge weight \(1/(m+1)\). Then:

- every upper-colour vertex has load \(1\), since it has \(m+1\)
  rooted occurrences;
- every tail \(T\) has load \((m-1)/(m+1)\), since it occurs once for
  each \(x\in X\setminus T\), of which there are \(m-1\);
- every head \(H\) also has load \((m-1)/(m+1)\).

For the head count, let \(q(H)=M_0^{-1}(H)\). Every other lower facet
\(L\subset H\), \(L\ne q(H)\), has

\[
M_0(L)=L\cup\{a\}
\]

with \(a\notin H\). If \(x=H\setminus L\), then the occurrence with
tail \(L\cup\{a\}\) and root \(x\) has head \(H\). This is a bijection
between the \(m-1\) lower facets of \(H\) other than \(q(H)\) and the
occurrences having head \(H\).

The total weight is

\[
\binom{2m-1}{m+1}
=\frac{m-1}{m+1}\binom{2m-1}{m}.
\]

Thus the unused capacity on either middle shore is exactly

\[
\frac2{m+1}\binom{2m-1}{m}
=\operatorname{Cat}_m.
\]

Consequently, for every \(M_0\), the relaxation of the distinct-upper
colour selector is perfectly balanced. The genuine open gate is its
integral rounding: choose one occurrence for every distinct upper
colour with no repeated tail or head, then use the \(\operatorname{Cat}_m\)
remaining tail/head slots for repeated-colour connector edges and the
global topology. Requiring every full colour fibre to be a matching is
a sufficient local regularity condition, but a much stronger one than
this global integral selector requires.

## 2. The punctured Steiner-system theorem

Fix \(y\in X\), and define

\[
\mathcal D_y=
\left\{
V\setminus\{y\}:
V\in\binom Xm,\ y\in V,\ a(V)=y
\right\}.
\tag{4}
\]

This is a family of \((m-1)\)-subsets of the \((2m-2)\)-point ground
set \(X\setminus\{y\}\).

### Lemma 2.1. Every \(m\)-set contains exactly one block

If every \(f_R\) is a permutation, then every

\[
T\in\binom{X\setminus\{y\}}m
\]

contains exactly one member of \(\mathcal D_y\).

#### Proof

Put \(R=T\cup\{y\}\). Since \(f_R\) is a permutation, the value \(y\)
has exactly one preimage \(x\in R\). This preimage cannot be \(x=y\),
because

\[
f_R(y)=a(T)\in T.
\]

Hence \(x\in T\), and

\[
a(R\setminus\{x\})=y.
\]

It follows that

\[
T\setminus\{x\}
=(R\setminus\{x\})\setminus\{y\}
\in\mathcal D_y.
\]

Conversely, any block of \(\mathcal D_y\) contained in \(T\) has the
form \(T\setminus\{x\}\) for a unique \(x\in T\), and gives a preimage
of \(y\) under \(f_R\). Hence there is exactly one such block. \(\square\)

### Lemma 2.2. \(\mathcal D_y\) is an \(S(m-2,m-1,2m-2)\)

#### Proof

Two distinct blocks of \(\mathcal D_y\) cannot contain the same
\((m-2)\)-set: their union would be an \(m\)-set containing two blocks,
contrary to Lemma 2.1.

Count incidences between blocks and containing \(m\)-sets. Each block
lies in exactly \(m-1\) such \(m\)-sets, and Lemma 2.1 says every
\(m\)-set contains one block. Therefore

\[
|\mathcal D_y|(m-1)=\binom{2m-2}{m}
                   =\binom{2m-2}{m-2}.
\tag{5}
\]

Each block contains exactly \(m-1\) subsets of size \(m-2\). Thus (5)
says that the total number of \((m-2)\)-subsets occurring in the blocks
is exactly \(\binom{2m-2}{m-2}\). Since none occurs twice, every one
occurs exactly once. This is precisely

\[
\mathcal D_y\cong S(m-2,m-1,2m-2).
\qquad\square
\]

In particular,

\[
|\mathcal D_y|
=\frac1{m-1}\binom{2m-2}{m-2}
=\frac1m\binom{2m-2}{m-1}
=\operatorname{Cat}_{m-1}.
\tag{6}
\]

## 3. Divisibility and the prime-semilevel obstruction

For a Steiner system \(S(t,b,v)\), counting blocks through a fixed
\(j\)-subset gives the necessary integer

\[
\lambda_j
=\frac{\binom{v-j}{t-j}}{\binom{b-j}{t-j}}
\qquad(0\le j\le t).
\tag{7}
\]

Substitute

\[
t=m-2,\qquad b=m-1,\qquad v=2m-2,
\]

and put \(\ell=t-j\). Then (7) becomes

\[
\boxed{
A_\ell(m):=
\frac1{\ell+1}\binom{m+\ell}{\ell}\in\mathbb Z
\qquad(0\le\ell\le m-2).
}
\tag{8}
\]

These divisibility conditions admit a clean exact characterization.

### Proposition 3.1. Conditions (8) hold for every \(\ell\) if and only if \(m\) is prime

Here \(m\ge2\).

#### Prime case

Use

\[
A_\ell(m)=\frac1m\binom{m+\ell}{\ell+1}.
\tag{9}
\]

If \(m\) is prime and \(0\le\ell\le m-2\), then \((\ell+1)!\) is
invertible modulo \(m\), while the numerator in

\[
\binom{m+\ell}{\ell+1}
=\frac{m(m+1)\cdots(m+\ell)}{(\ell+1)!}
\]

contains a factor \(m\). Hence the binomial coefficient is divisible
by \(m\), so (9) is integral.

#### Composite case

Let \(p\) be a prime divisor of composite \(m\), and take
\(\ell=p-1\). Since \(p\le m/2\), this lies in the required range.
Modulo \(p\),

\[
\binom{m+p-1}{p-1}
=\prod_{i=1}^{p-1}\frac{m+i}{i}
\equiv1\pmod p.
\tag{10}
\]

It is therefore not divisible by \(p\), and

\[
A_{p-1}(m)=\frac1p\binom{m+p-1}{p-1}
\]

is not an integer. This violates (8). \(\square\)

Consequently,

\[
\boxed{
\text{all local maps }f_R\text{ can be permutations only if }
m=\frac{k+1}{2}\text{ is prime.}
}
\tag{11}
\]

Some immediate subfamilies are:

- \(\ell=1\) gives \((m+1)/2\in\mathbb Z\), excluding every even
  \(m\ge4\), hence every \(k\equiv3\pmod4\) in that range;
- \(\ell=2\) gives \((m+1)(m+2)/6\in\mathbb Z\), excluding every
  composite case with \(3\mid m\) once this row is present.

At \(k=17\), one has \(m=9\). The \(\ell=2\) condition is

\[
A_2(9)=\frac13\binom{11}{2}=\frac{55}{3},
\]

which is not an integer. Therefore no predecessor perfect matching
\(M_0\) at \(k=17\) can make every local map \(f_R\) a permutation.

Primality is only divisibility admissibility. No converse existence
claim is made for prime \(m\).

### 3.2. A quantitative collision consequence

The composite obstruction forces more than one isolated failed value.
For fixed \(y\) and

\[
T\in\binom{X\setminus\{y\}}m,
\]

put

\[
c_y(T)=\#\{B\in\mathcal D_y:B\subset T\}.
\tag{12}
\]

Equivalently, \(c_y(T)\) is the indegree of the value \(y\) under
\(f_{T\cup\{y\}}\). Since every block is contained in \(m-1\) such
\(m\)-sets,

\[
\sum_T(c_y(T)-1)
=(m-1)\bigl(|\mathcal D_y|-\operatorname{Cat}_{m-1}\bigr).
\tag{13}
\]

If \(m\) is composite, the left-hand vector cannot vanish identically,
by the Steiner obstruction. If \(|\mathcal D_y|\) has the Catalan
value, its nonzero entries sum to zero and hence

\[
\sum_T|c_y(T)-1|\ge2.
\]

If the size is not Catalan, (13) is a nonzero multiple of \(m-1\), so
the same lower bound holds for composite \(m\ge4\). Therefore every
coordinate satisfies

\[
\sum_T|c_y(T)-1|\ge2.
\tag{14}
\]

Globally,

\[
\sum_y|\mathcal D_y|=\binom{2m-1}{m}
\]

and

\[
(m-1)\binom{2m-1}{m}
=(2m-1)\binom{2m-2}{m},
\]

so the total signed sum of all \(c_y(T)-1\) is zero. Hence (14) gives

\[
\boxed{
\sum_{R\in\binom X{m+1}}
\bigl((m+1)-|\operatorname{im}f_R|\bigr)
\ge 2m-1
}
\tag{15}
\]

for every composite \(m\). Indeed, for a function on an \((m+1)\)-set,
the number of missing image values equals the total positive indegree
excess.  Since its indegrees sum to \(m+1\), its total negative deficit
is the same number.  Therefore, exactly,

\[
 \sum_{y\in R}|c_y(R\setminus\{y\})-1|
 =2\bigl((m+1)-|\operatorname{im}f_R|\bigr).
\]

Summing this identity over \(R\) turns the lower bound
\(2(2m-1)\) from (14) into (15).

At \(k=17\), the aggregate head-collision deficiency is therefore at
least \(17\). Since \(f_R(x)\ne x\), its image has at least two values,
so one upper colour contributes at most \(m-1\) to (15). Thus at least
three distinct upper colours must be locally non-simple.

## 4. Exact converse formulation: a compatible punctured Steiner family

The preceding obstruction is not merely a loose shadow count. It gives
an exact reformulation of the strong ansatz.

For a family \((\mathcal D_y)_{y\in X}\), define the labelled incidence
set

\[
\mathcal I=
\left\{
\bigl(L,L\cup\{y\}\bigr):
y\notin L,\ L\in\mathcal D_y
\right\}
\subseteq\mathcal L\times\mathcal M.
\tag{16}
\]

Then the following are equivalent:

1. there is a predecessor perfect matching \(M_0\) for which every
   \(f_R\) is a permutation;
2. for every \(y\), \(\mathcal D_y\) is an
   \(S(m-2,m-1,2m-2)\) on \(X\setminus\{y\}\), and \(\mathcal I\) is a
   perfect matching between \(\mathcal L\) and \(\mathcal M\).

The forward direction is Lemma 2.2 together with

\[
L\in\mathcal D_y
\iff M_0(L)=L\cup\{y\}.
\]

For clarity, the containment assertion needed in the converse is automatic
for these special Steiner parameters, but it is not a generic property of
Steiner systems.  Put \(b=m-1\), and let \(Y\) be its \(2b\)-point
ground set.  In any \(S(b-1,b,2b)\), two blocks intersect in at most
\(b-2\) points.  Since

\[
 |B^c\cap C^c|=|B\cap C|
 \qquad(B^c=Y\setminus B),
\]

the complements of the blocks are again a packing of \((b-1)\)-sets.
They have the same number of blocks, and hence cover

\[
 |\mathcal D_y|\binom b{b-1}=\binom{2b}{b-1}
\]

such sets; therefore the complementary blocks form another
\(S(b-1,b,2b)\).  If \(T\) is a \((b+1)\)-set, its complement
\(T^c\) is a \((b-1)\)-set and lies in a unique complementary block
\(B^c\).  Equivalently, the original block \(B\) lies in \(T\).
There cannot be two such blocks, since two distinct \(b\)-subsets of one
\((b+1)\)-set intersect in at least \(b-1\) points.  Thus every
\(m\)-set contains exactly one block.

Now use \(\mathcal I\) as \(M_0\). For fixed \(R\) and \(y\in R\),
the preceding special-parameter argument says that the \(m\)-set
\(R\setminus\{y\}\) contains exactly one block of \(\mathcal D_y\).
It is \(R\setminus\{x,y\}\) for a unique \(x\ne y\), and therefore

\[
f_R(x)=y.
\]

Every \(y\in R\) has exactly one preimage, so \(f_R\) is a permutation.

The perfect-matching compatibility in (16) is an additional condition;
the existence of the individual Steiner systems does not supply it.
In particular, even a prime value of \(m\) for which the individual
designs exist would still leave a nontrivial simultaneous-resolution
problem.

### 4.1. The compatibility condition one rank lower

The extra compatibility has a useful local form. Fix

\[
S\in\binom{X}{m-2}.
\]

For each \(y\in X\setminus S\), the Steiner system \(\mathcal D_y\)
contains a unique block through \(S\). Write it as

\[
S\cup\{\phi_S(y)\}\in\mathcal D_y.
\tag{17}
\]

Then \(\phi_S\) is a permutation of the \((m+1)\)-point set
\(X\setminus S\). Indeed, the unique-preimage condition for a value
\(z\) is exactly the assertion that the lower set \(S\cup\{z\}\) has
one matching extension in (16).

Moreover, \(\phi_S\) has neither fixed points nor 2-cycles. A fixed
point is impossible because every block of \(\mathcal D_y\) avoids
\(y\). If

\[
\phi_S(y)=z,\qquad \phi_S(z)=y,
\]

then both lower sets \(S\cup\{z\}\) and \(S\cup\{y\}\) would be matched
to the same middle set \(S\cup\{y,z\}\), contradicting (16).

Thus compatibility of the punctured Steiner systems forces, around
every \((m-2)\)-core, a permutation whose cycles all have length at
least three. This is a consequence of the desired matching, not a
converse construction.

## 5. Exact cyclic reduction

Let \(X=\mathbb Z_{2m-1}\). If \(M_0\) is rotation-equivariant, then

\[
\mathcal D_y=y+\mathcal D_0.
\tag{18}
\]

Thus an equivariant construction of the strong ansatz is equivalent to
choosing one base design

\[
\mathcal D_0\cong S(m-2,m-1,2m-2)
\quad\text{on }X\setminus\{0\},
\]

such that the orbit incidence set

\[
\left\{
\bigl(B+y,(B+y)\cup\{y\}\bigr):
B\in\mathcal D_0,\ y\in X
\right\}
\tag{19}
\]

is a perfect matching between \(\mathcal L\) and \(\mathcal M\).

Equivalently, both endpoint conditions must hold:

\[
\#\left\{
y\notin L:\ (-y)+L\in\mathcal D_0
\right\}=1
\qquad(L\in\mathcal L),
\tag{20}
\]

and

\[
\#\left\{
y\in V:\ (-y)+(V\setminus\{y\})\in\mathcal D_0
\right\}=1
\qquad(V\in\mathcal M).
\tag{21}
\]

No cyclic, modular, or symmetric-chain rule can evade the divisibility
obstruction: if it makes all local maps permutations, it necessarily
produces the designs above. Conversely, (18)--(21) are a precise target,
not an existence theorem.

## 6. Consequence for the general construction programme

The all-colour local-permutation condition is too strong to serve as a
uniform all-odd-dimensional invariant: it already fails whenever
\((k+1)/2\) is composite, including the first open case \(k=17\).

Therefore an all-dimensional colour--tail--head construction must allow
at least one of the following:

- repeated heads inside some full upper-colour occurrence classes;
- selection of only a proper subset of the rooted occurrences of a
  colour;
- occurrence splitting or a multi-component factor followed by a
  global splice;
- a global selector that resolves collisions across colours rather than
  demanding that every colour class be locally simple in advance.

This conclusion is compatible with the separate source-overlap warning:
a bounded-defect construction cannot be reduced to a sparse bank of
\(O(1)\) local rails. The theorem here concerns a global incidence
regularity condition and shows that one particularly attractive global
regularity condition is itself arithmetically impossible in most
dimensions.

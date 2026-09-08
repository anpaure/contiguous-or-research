# Gate C: deletion-deck rigidity for antipodal block shuffles

**Status (2026-08-22).**  Every assertion below is proved.  For every
cyclic-successor row of a signed antipodal permutation, the `b-1` coherent
middle flags form a deletion deck of one `(b+1)`-set.  Their exact factor
overlap is governed by a single statistic: the last proper prefix at which
the undeleted walk has height at most two.

If a block-shuffle phase has loss `L=O(bK)`, then, outside at most
`L/D` rows, that last low prefix occurs by time `2D+2`.  Taking
`D=sqrt(bK)` shows that for every `K=o(b)`, all but `o(b)` rows of a
high-overlap shuffle must escape above height two within `o(b)` steps and
never return.  This is the exact analytic rigidity condition missing from
the block-entropy ledger.

The theorem does not yet count permutations satisfying this simultaneous
early-escape condition.  It reduces the live multiplicity gate to that
count.

Throughout,
\[
 n=2b,qquad b\ge3\text{ odd},qquad q=b(b-1).             \tag{0.1}
\]

## 1. A primitive-Dyck deletion deck

Let `S subseteq Z_(2b)` have size `b+1`, contain `p`, and omit the cyclic
predecessor `p-1`.  Rotate coordinates so that `p` is position zero.  Let
\[
 F_S(\ell)=2|S\cap[p,p+\ell-1]|-\ell,
 \qquad 0\le\ell\le2b.                                  \tag{1.1}
\]
Thus `F_S(0)=0`, `F_S(2b)=2`, and the first step is positive.

For `y in S\{p}`, write
\[
                         d(y)=(y-p)\bmod {2b}.            \tag{1.2}
\]
Deleting `y` changes the rotated prefix height to
\[
 F_{S\setminus\{y\}}(\ell)
 =F_S(\ell)-2\mathbf1_{\ell>d(y)}.                       \tag{1.3}
\]

### Lemma 1.1 (exact deletion criterion)

For `y in S\{p}`, the flag with predecessor arc `p->p-1` and middle
`S\{y}` belongs to the
Catalan-switched factor if and only if
\[
\begin{aligned}
 F_S(\ell)&>0 &&(1\le\ell\le d(y)),\\
 F_S(\ell)&>2 &&(d(y)<\ell<2b).                          \tag{1.4}
\end{aligned}
\]

#### Proof

For a cyclic predecessor arc, factor membership is equivalent to the
middle word rotated at `p` being primitive Dyck.  Its proper prefix heights
must therefore be positive.  Substitute (1.3), separately before and after
the deleted step.  The final height is automatically
`F_S(2b)-2=0`. \(\square\)

If `F_S` ever has a nonpositive proper prefix, no deletion works: a later
deletion leaves that prefix unchanged, while an earlier deletion lowers it
by two.  Hence assume
\[
                         F_S(\ell)>0\quad(1\le\ell<2b).   \tag{1.5}
\]
Define the last-low time
\[
 \lambda(S)=\max\{\ell<2b:F_S(\ell)\le2\}.              \tag{1.6}
\]
This set is nonempty because `F_S(1)=1`.

### Corollary 1.2 (last-low classification)

Under (1.5), deletion of `y` is valid if and only if
\[
                         d(y)\ge\lambda(S).               \tag{1.7}
\]
Moreover `F_S(lambda(S))=2`, the suffix after that prefix has equally many
plus and minus steps, and
\[
 |\{y\in S:d(y)\ge\lambda(S)\}|={2b-\lambda(S)\over2}.  \tag{1.8}
\]

#### Proof

Condition (1.5) supplies the first line of (1.4).  The second line holds
exactly when the deletion occurs no earlier than the last prefix of height
at most two, proving (1.7).

At the last-low time the height cannot be one: the next step would reach
at most two again, contradicting maximality (and the last proper height is
three because the final height is two).  Thus it is two.  The remaining
walk returns from height two to height two, so it contains equally many
plus and minus steps.  Its length is `2b-lambda(S)`, proving (1.8).
\(\square\)

If only a prescribed deletion set `Y subseteq S` is available, its exact
valid count is therefore
\[
 m(S,Y)=
 \begin{cases}
 0,&\min_{1\le\ell<2b}F_S(\ell)\le0,\\
 |\{y\in Y:d(y)\ge\lambda(S)\}|,&\text{otherwise}.
 \end{cases}                                             \tag{1.9}
\]
In particular, when `|Y|=b-1`,
\[
 m(S,Y)\ge b-1-D\quad\Longrightarrow\quad
                         \lambda(S)\le2D+2.              \tag{1.10}
\]
Indeed (1.8) bounds `m(S,Y)` by
`b-lambda(S)/2`.

## 2. Rows of a signed antipodal permutation

Write an antipodal permutation as
\[
 \pi(x)=\alpha(x)+b\epsilon_x\pmod {2b},qquad
 \pi(x+b)=\pi(x)+b,                                      \tag{2.1}
\]
where `alpha in S_b`.  Put
\[
 P_x=\alpha(x)+\epsilon_x\pmod2,qquad
                         c_x=P_x+x\pmod2.                \tag{2.2}
\]

Call a residue row `r in Z_b` *good* when
\[
 \alpha(r)=\alpha(r-1)+1\pmod b,qquad c_r=c_{r-1}.       \tag{2.3}
\]

### Lemma 2.1 (a good row has a predecessor deletion deck)

For a good row,
\[
                         \pi(r)=\pi(r-1)+1\pmod {2b}.    \tag{2.4}
\]
Put
\[
 S_r=\{\pi(r+u):0\le u\le b\},qquad
 Y_r=\{\pi(r+t):1\le t<b\}.                             \tag{2.5}
\]
Then `|S_r|=b+1`, `|Y_r|=b-1`, and the coherent flag in row `r`, column
`t`, has predecessor arc `pi(r)->pi(r)-1` and middle
\[
                         S_r\setminus\{\pi(r+t)\}.        \tag{2.6}
\]
Consequently its exact row overlap is `m(S_r,Y_r)` from (1.9).

#### Proof

The two residues in (2.3) are consecutive.  The equality of the corrected
parities says that `pi(r)` and `pi(r-1)` have opposite coordinate parity.
Among the two antipodal coordinates with the successor residue, exactly one
has parity opposite `pi(r-1)`; it is `pi(r-1)+1`.  This proves (2.4).

The interval `r+[0,b]` contains both members of one antipodal pair and one
member of every other pair, so its image has size `b+1`; removing the two
end columns gives `|Y_r|=b-1`.  The canonical coherent middle is
`r+([0,b]\{t})`, and applying `pi` gives (2.6).  Lemma 1.1 now applies.
\(\square\)

Let
\[
 B(\alpha)=|\{r:\alpha(r)\ne\alpha(r-1)+1\}|,qquad
 T(c)=|\{r:c_r\ne c_{r-1}\}|.                            \tag{2.7}
\]
At most `B(alpha)+T(c)` rows are not good.

## 3. High overlap forces simultaneous early escape

For either coherent phase, fixed `t` and the stage variable run once
through every residue row.  Antipodal translation gives the identical
relative deletion deck in the two lifts of a good row.  Let `m_r` be its
exact row overlap from Lemma 2.1.

### Theorem 3.1 (row-rigidity reduction)

Suppose one phase of `pi(H*)` has overlap at least `q-L`.  Then
\[
 \sum_{r\text{ good}}(b-1-m_r)\le L.                    \tag{3.1}
\]
For every `1<=D<b-1`, all but at most `L/D` good rows satisfy
\[
 m_r\ge b-1-D,qquad
 F_{S_r}(\ell)>0\ (1\le\ell<2b),qquad
                         \lambda(S_r)\le2D+2.            \tag{3.2}
\]

#### Proof

The total phase deficit is the sum of nonnegative row deficits.  Keeping
only the good rows gives (3.1).  Markov's inequality leaves at most `L/D`
rows with deficit greater than `D`.  A remaining row has positive base
walk, since otherwise (1.9) would give `m_r=0`; then (1.10) gives the last
claim. \(\square\)

### Corollary 3.2 (coefficient-one scale)

If
\[
 L\le CbK,qquad K=o(b),qquad
 B(\alpha)+T(c)=O(K),                                    \tag{3.3}
\]
take `D=sqrt(bK)`.  Apart from
\[
 O(K)+O(\sqrt{bK})=o(b)                                  \tag{3.4}
\]
rows, every deletion-deck walk is positive and has
\[
                         \lambda(S_r)=O(\sqrt{bK})=o(b). \tag{3.5}
\]

Thus a candidate family at `K=c b/log b` cannot rely only on its
`exp((c+o(1))b)` block entropy.  Almost every cyclic cut of almost every
selected block order must produce a transported transversal walk that
rises above height two within `o(b)` steps and never returns.

## 4. Exact remaining counting theorem

Let `R_{b,K,D}` be the signed antipodal permutations satisfying
`B(alpha)+T(c)<=K` for which all but `D` good rows obey
`lambda(S_r)<=D`.  Theorem 3.1 reduces the live multiplicity gate to the
asymptotic size and incidence profile of this explicit finite set.

At the entropy-viable scale `K=Theta(b/log b)`, a positive result needs
\[
 |R_{b,K,o(b)}|\ge {4^b\over\operatorname{poly}(b)}       \tag{4.1}
\]
together with a rankwise matching theorem.  An upper bound
`|R_{b,K,o(b)}|=2^{b+o(b)}` (or any exponent below `b log 4`) would close
the entire antipodal block-shuffle route.  No such count is asserted here.

## 5. Finite audit

The companion checker
`scratch/verify_gate_c_block_shuffle_row_rigidity_20260822.py` exhausts
all deletion decks through `b=6`, verifies the exact last-low formula,
and checks the good-row predecessor/deck identity over full small signed
wreaths.  It is confirmatory; all proofs are above.

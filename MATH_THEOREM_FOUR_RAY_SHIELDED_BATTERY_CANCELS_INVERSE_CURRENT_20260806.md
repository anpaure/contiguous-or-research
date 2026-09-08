# Four shielded ray ports exactly cancel the proper lower inverse-pair current

**Date:** 2026-08-06  
**Method:** literal interval-union calculation  
**Status:** unconditional word-level **proper-lower** absorber.  It converts
the complete lower two-rail current into a state swap on four pivot letters.
The same linear word has zero changed central/upper intervals and therefore
does **not** cancel the complementary upper current of the native wreath
move.  A dual battery or a complement-paired owner-cycle embedding is still
required.  The note also does not embed the four chain blocks in a
length-`B(k)+O(1)` resident owner carrier.

## 1. One shielded ray port

Fix two active coordinates `a,d` and put

\[
                         H=\{a,d\}.                   \tag{1.1}
\]

For an ordered list `Z=(z_1,...,z_t)` disjoint from `H`, consider the word
block

\[
       H,\ \{p\},\ \{z_1\},\ldots,\{z_t\},\ H,
              \qquad p\in\{a,d\}.                    \tag{1.2}
\]

The two copies of `H` are fixed.  Compare the states `p=a` and `p=d`.

### Lemma 1.1 (exact one-sided ray current)

The complete signed change of the interval-union multiset of (1.2), after
changing `p=a` to `p=d`, is

\[
        \sum_{j=0}^{t}
        \left([\{z_1,\ldots,z_j,d\}]
                    -[\{z_1,\ldots,z_j,a\}]\right).   \tag{1.3}
\]

#### Proof

An interval not containing the pivot is unchanged.  An interval containing
the pivot and either shield contains both `a` and `d`, so it is unchanged.
Every remaining interval containing the pivot starts at the pivot and ends
after exactly `j` chain letters.  Its two values are the two sets in
(1.3).  These are all possibilities.  \(\square\)

Several ports may be concatenated while sharing their adjacent shields.
Any interval meeting two ports contains the shield between them and is
therefore invariant.

## 2. The four-port battery

Use the inverse-pair notation

\[
 |X|=m-2=:p,qquad |Y|=m-1=p+1.                       \tag{2.1}
\]

Prepare four shielded ports whose chain orders are

\[
\begin{array}{c|c}
\text{port}&\text{chain}\ \hline
Y^+&(y_{p+1},y_p,\ldots,y_2)\\
Y^-&(y_1,y_2,\ldots,y_p)\\
X^+&(x_p,x_{p-1},\ldots,x_1)\\
X^-&(x_1,x_2,\ldots,x_p).
\end{array}                                             \tag{2.2}
\]

The first `j` chain letters in these ports are respectively the suffix or
prefix profiles `Y_j^+,Y_j^-,X_j^+,X_j^-`.

Let battery state `B_0` assign

\[
        d\text{ to the }Y^+,X^+\text{ pivots},qquad
        a\text{ to the }Y^-,X^-\text{ pivots},          \tag{2.3}
\]

and let `B_1` swap all four pivot labels.

For `0<=j<=p`, the native inverse-pair current is

\[
\begin{aligned}
 \mathcal D_j(X,Y;a,d)={}&
 [Y_j^++d]+[Y_j^-+a]-[Y_j^++a]-[Y_j^-+d]\\
 &+[X_j^-+a]+[X_j^++d]-[X_j^-+d]-[X_j^++a].           \tag{2.4}
\end{aligned}
\]

### Theorem 2.1 (exact proper-lower battery cancellation)

The complete changed interval current of the battery transition
`B_0 -> B_1`, in ranks `1,...,m-1`, is

\[
                         -\mathcal D_j(X,Y;a,d)        \tag{2.5}
\]

at every proper length `j+1`.  Consequently, performing the native
inverse-pair move and the battery swap simultaneously has zero complete
proper lower current.

#### Proof

Apply Lemma 1.1 to the four chains (2.2).  Under (2.3), the `Y^+` and
`X^+` ports change from `d` to `a`, while the `Y^-` and `X^-` ports change
from `a` to `d`.  The resulting sum is

\[
\begin{aligned}
 &[Y_j^++a]-[Y_j^++d]+[X_j^++a]-[X_j^++d]\\
 &\quad+[Y_j^-+d]-[Y_j^-+a]+[X_j^-+d]-[X_j^-+a],
\end{aligned}
\]

which is the negative of (2.4).  At `j=0` the four singleton changes cancel;
at `j=p` the two full-`X` terms cancel, exactly as in the native current.
Lemma 1.1 also proves that no unlisted changed lower interval is created by
the shielded ports. \(\square\)

### Proposition 2.2 (the same linear battery has no upper current)

Every interval whose value changes under `B_0 -> B_1` avoids both shields
of one port.  It is therefore the pivot followed by at most `p=m-2` chain
letters and has rank at most

\[
                              p+1=m-1.                \tag{2.6}
\]

Hence the battery has zero changed interval current in ranks `m` and
above.  In particular, it cannot by itself cancel a nonzero upper current
of the native inverse-pair move.

#### Proof

If an interval containing a changed pivot meets either adjacent shield,
then it contains `H={a,d}` and its union is independent of the pivot state.
If it avoids both shields, Lemma 1.1 says it consists of the pivot and a
prefix of that port's chain.  This proves (2.6) and the assertion. \(\square\)

The upper wreath current is obtained by **taking complements** of the
native lower basis sets.  Complementation is an algebraic bijection between
the two native ledgers; it is not an operation performed by the linear
battery word.  Thus lower cancellation does not imply physical upper
cancellation.

The transition is involutive.  Thus the same four physical pivot positions
can absorb arbitrarily many back-and-forth uses of one fixed native slot;
the battery does not accumulate rail debt.

## 3. Size and the exact host obligation

As a standalone source block, four ports sharing consecutive shields use

\[
                       4p+4+5=4m+1                 \tag{3.1}
\]

positions: `4p` chain letters, four pivot letters, and five shields.  The
chain support is `O(m)=O(d^2)`, but it need not be **extra** support.  In a
near-optimal construction the intended use is to prepare the four ordered
chains inside the existing chronology and add only the bounded pivot/shield
interface.

This separates the remaining physical theorem cleanly:

> **Prepared four-ray battery host.**  Plant the four chain segments (2.2)
> inside the owner/source chronology, with their shields and pivots
> replacing existing local support except for `O(1)` positions, while
> preserving central ownership, q1 palettes, residence, and the transported
> background compiler.

The sharp monotone-pivot packet proves that a fixed number of nested ray
ports can be made owner-legal and resident locally, and protected-factor
theorems can plant fixed `O(m)` central support.  Those results do not yet
prove that the four ports in (2.2), the chosen native companion slot, and
one common global upper/compiler completion coexist in the same
near-optimal chronology.

For true all-width closure, append one further host requirement:

> **Complementary dual-battery hypothesis.**  In the same protected
> occurrence state, plant a second shielded gadget whose changed upper
> occurrence ledger is the negative of the complemented native current,
> whose lower current is zero, and whose cross-gadget intervals are fixed;
> equivalently, embed the battery in a complement-paired cyclic owner
> system carrying an occurrence-preserving bijection
> `S -> Omega-S` for every signed ray occurrence.

`MATH_THEOREM_DUAL_FOUR_RAY_UPPER_BATTERY_AND_FORMAL_ALLWIDTH_CLOSURE_20260806.md`
constructs the required upper dual explicitly, with all pivot letters of
rank at most `m+1`, and combines the two batteries into one shield-isolated
eight-port block.  What remains conditional is its coinstantiation with
the native factor occurrence: the host must make every cross-native/battery
interval invariant and preserve occurrence capacities.  Thus
**proper-lower current absorption is literal and stateful**, the upper dual
is also literal, and the remaining issues are common-host coinstantiation
and changing-slot connectivity.

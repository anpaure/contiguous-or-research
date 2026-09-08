# The ECO seams do not collapse by duplicate counting

## 1. Outcome

The critical Catalan recurrence in `CRITICAL_CATALAN_LIFT.md` asks that the
*uncharged missing* targets created by an ECO lift have Cesaro
`o(Cat_m)` size.  A tempting shortcut is to count all path-local seam
targets and hope that, after forgetting their owners, they collapse to only
`o(Cat_m)` distinct masks.

That shortcut is false already in the terminal-peak ECO family and already
at shadow depth one.

### Theorem 1 (three distinct lower seams per parent)

Let `F_m` be the MSW wreath factor on `2m+1` coordinates, indexed by Dyck
words `w in D_m`.  In the terminal ECO child

\[
                              w\longmapsto w10,       \tag{1.1}
\]

the lower depth-one row contains exactly three windows which use neither of
the two inserted coordinates.  Over all `w in D_m`, these are

\[
                              3\operatorname{Cat}_m  \tag{1.2}
\]

pairwise distinct masks.  Their complements give another
`3 Cat_m` pairwise distinct upper depth-one seam masks containing both new
coordinates.

Consequently, any proof which simply declares every nontransported ECO seam
value exceptional has

\[
                              B_{m,1}\ge3\operatorname{Cat}_m,     \tag{1.3}
\]

and cannot meet the sub-Catalan condition of the critical lift theorem.

This is a no-go for **duplication-only seam accounting**, not for the
critical ECO programme itself.  The masks in Theorem 1 are actual windows,
so they are covered.  A successful recurrence may certify them directly
and pay nothing for them.  What it may not do is leave all seam provenance
unresolved and hope that distinctness alone turns `Theta(Cat_m)` raw seams
into `o(Cat_m)` targets.

## 2. The two antipodal insertion gaps

Write the parent MSW flip order as

\[
                         \rho(w)=(r_1,\ldots,r_{2m}),               \tag{2.1}
\]

and denote the distinguished closing coordinate by `z`.  The ordinary
wreath coordinate order is

\[
 C(w)=(z,r_2,r_4,\ldots,r_{2m},r_1,r_3,\ldots,r_{2m-1}).          \tag{2.2}
\]

For the terminal child, put `p=2m+1` and `q=2m+2`.  Concatenation locality
of the MSW flip order gives

\[
 \rho(w10)=(r_1,\ldots,r_{2m},q,p),                 \tag{2.3}
\]

up to the harmless convention which names the inserted `1` and `0` in the
opposite order.  After the standard step-two reindexing, its wreath order is

\[
 C(w10)=
 (z,r_2,\ldots,r_{2m},p,r_1,r_3,\ldots,r_{2m-1},q).                \tag{2.4}
\]

Thus `C(w10)` is obtained from `C(w)` by inserting `p` and `q` in two
nearly antipodal gaps.  Removing the two inserted letters leaves two old
arcs:

\[
 \begin{aligned}
 R_0&=(r_1,r_3,\ldots,r_{2m-1}), &&|R_0|=m,\\
 R_1&=(z,r_2,r_4,\ldots,r_{2m}), &&|R_1|=m+1.
 \end{aligned}                                      \tag{2.5}
\]

## 3. Proof of Theorem 1

In dimension `2m+3`, a lower depth-one wreath value is a cyclic interval of
length `m` in (2.4).  Such an interval avoids both inserted coordinates
exactly when it is contained in one of the two old arcs (2.5).

There is one length-`m` interval in the arc of length `m`, and there are two
length-`m` intervals in the arc of length `m+1`.  Hence every terminal child
has exactly

\[
                              1+2=3                              \tag{3.1}
\]

zero-inserted-coordinate seam windows.

After `p,q` are deleted, all three are length-`m` cyclic intervals in the
parent order `C(w)`.  They are therefore three middle-layer members of the
parent wreath.  The MSW wreath factor partitions the entire rank-`m` layer:
no middle member occurs in two parent wreaths, and the `2m+1` middle members
within one wreath are distinct.  It follows that the three windows for
different `w` are all distinct, proving (1.2).

For every cyclic coordinate order, complementation maps a length-`m`
interval in `2m+3` coordinates to the corresponding upper depth-one
interval of length `m+3`.  The complements of the windows just counted all
contain `p,q`, and complementation is injective.  This proves the upper
statement.  \(\square\)

## 4. The same calculation at arbitrary fixed depth

The exact local count is useful beyond depth one.  At lower depth `j>=1`,
the child windows have length

\[
                              \ell=m+1-j.             \tag{4.1}
\]

The number avoiding `p,q` is

\[
 (m-\ell+1)+(m+1-\ell+1)=j+(j+1)=2j+1.             \tag{4.2}
\]

So a terminal child has `2j+1` raw lower seam windows, and the same number
of complementary upper ones.  At `j=1` they lie in the parent middle layer,
whose exact partition makes global distinctness immediate.  At larger
depths the parent factor may have collisions, so (4.2) alone does not give
`(2j+1)Cat_m` distinct masks.  This is precisely why depth one is the clean
all-dimensional obstruction to a duplication-only argument.

## 5. Correct consequence for the critical lift

The critical Catalan theorem remains viable, but its charging lemma must be
targetwise.  At every ECO seam it must do one of the following:

1. certify the seam value as actually covered and remove it from the defect
   ledger;
2. charge a genuinely missing value to a specified old missing value under
   a specified child injection; or
3. place it in a residual family whose **missing**, not merely unresolved,
   distinct count is Cesaro `o(Cat_m)`.

Theorem 1 rules out replacing these steps by the sentence “there are only
`o(Cat_m)` distinct seam targets after deduplication.”  There are already
`3 Cat_m` distinct targets in one of the two simplest Catalan-sized child
families.
